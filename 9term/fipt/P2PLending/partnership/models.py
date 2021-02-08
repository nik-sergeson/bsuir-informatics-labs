from datetime import date, timedelta
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models, transaction
from djmoney.models.fields import MoneyField

from P2PLending.lending.models import MoneyRequestAd, MoneyProposalAd, MoneyRequest, MoneyProposal, Recommendation
from P2PLending.partnership.exceptions import MoneyPartnershipException, SuggestionException
from P2PLending.users.models import User, UserMoney


class SuggestionStatus(models.Model):
    SUGGESTED = 'SUG'
    ACCEPTED = 'ACC'
    REJECTED = 'REJ'
    CANCELLED = 'CAN'
    STATUS_CHOICES = (
        (SUGGESTED, 'Suggested'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (CANCELLED, 'Cancelled')
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=SUGGESTED)

    class Meta:
        abstract = True

    def reject(self):
        self.status = self.REJECTED
        self.save()

    def accept(self):
        self.status = self.ACCEPTED
        self.save()

    def cancel(self):
        self.status = self.CANCELLED
        self.save()

    @property
    def is_suggested(self):
        return self.status == self.SUGGESTED

    @property
    def is_accepted(self):
        return self.status == self.ACCEPTED

    @property
    def is_rejected(self):
        return self.status == self.REJECTED

    @property
    def is_cancelled(self):
        return self.status == self.CANCELLED


class MoneyProposalPartnershipSuggestion(MoneyRequest, SuggestionStatus):
    proposal = models.ForeignKey(MoneyProposalAd)
    from_request = models.ForeignKey(MoneyRequestAd, null=True)

    @property
    def can_be_accepted(self):
        return MoneyProposalPartnership.can_be_concluded(self)

    def accept(self):
        if self.can_be_accepted:
            with transaction.atomic():
                suggestions = MoneyProposalPartnershipSuggestion.objects.filter(proposal=self.proposal).exclude(
                    id=self.id)
                for suggestion in suggestions:
                    suggestion.reject()
                super().accept()
        else:
            raise SuggestionException("Can't accept suggestion")

    def validate(self):
        if self.proposal.is_closed:
            raise ValidationError("Target proposal is closed")
        if self.from_request and self.from_request.is_closed:
            raise ValidationError("Request from created is closed")
        super().clean()

    @classmethod
    def get_for_proposal(cls, proposal, **kwargs):
        return list(
            filter(lambda x: x.from_request is None or x.from_request.is_opened,
                   cls.objects.filter(proposal=proposal, **kwargs)))


class MoneyRequestPartnershipSuggestion(MoneyProposal, SuggestionStatus):
    request = models.ForeignKey(MoneyRequestAd)
    from_proposal = models.ForeignKey(MoneyProposalAd, null=True)

    @property
    def can_be_accepted(self):
        return MoneyRequestPartnership.can_be_concluded(self)

    def accept(self):
        if self.can_be_accepted:
            with transaction.atomic():
                suggestions = MoneyRequestPartnershipSuggestion.objects.filter(request=self.request).exclude(id=self.id)
                for suggestion in suggestions:
                    suggestion.reject()
                super().accept()
        else:
            raise SuggestionException("Can't accept suggestion")

    def validate(self):
        if self.request.is_closed:
            raise ValidationError("Target request is closed")
        if self.from_proposal and self.from_proposal.is_closed:
            raise ValidationError("Proposal from created is closed")
        super().clean()

    @classmethod
    def get_for_request(cls, request, **kwargs):
        return list(
            filter(lambda x: x.from_proposal is None or x.from_proposal.is_opened,
                   cls.objects.filter(request=request, **kwargs)))


class MoneyPartnership(models.Model):
    STARTED = "STR"
    FINISHED = "FIN"
    CANCELLED = "CAN"
    STATUS_CHOICES = (
        (STARTED, 'Started'),
        (FINISHED, 'Finished'),
        (CANCELLED, 'Cancelled')
    )
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=STARTED)
    borrower = models.ForeignKey(User, related_name="borrower")
    creditor = models.ForeignKey(User, related_name="creditor")
    amount = MoneyField(max_digits=10, decimal_places=2)
    dept = MoneyField(max_digits=10, decimal_places=2, default=0)
    annuity_payment = MoneyField(max_digits=10, decimal_places=2)
    rate = models.FloatField()
    term = models.DurationField()
    last_annuity_payment = models.DateField(null=True)
    last_dept_day_included = models.DateField(null=True)
    cancel_borrower_approved = models.BooleanField(default=False)
    cancel_creditor_approved = models.BooleanField(default=False)

    @classmethod
    def get_annuity_factor(cls, rate, term):
        rate /= 100
        return rate / (1 - (1 + rate) ** (-term.days))

    @classmethod
    def get_annuity_payment(cls, amount, rate, term):
        return amount * cls.get_annuity_factor(rate, term)

    @property
    def is_started(self):
        return self.status == self.STARTED

    @property
    def is_finished(self):
        return self.status == self.FINISHED

    @property
    def is_cancelled(self):
        return self.status == self.CANCELLED

    @property
    def borrower_dept(self):
        self.update_dept_if_necessary()
        return self.dept

    @property
    def has_dept(self):
        self.update_dept_if_necessary()
        return self.borrower_dept.amount > 0

    @property
    def annuity_payment_completed(self):
        return self.last_annuity_payment is not None and self.last_annuity_payment >= self.creation_time.date() + self.term

    def create_transaction(self, amount):
        return MoneyTransaction.objects.create(source_user=self.borrower, target_user=self.creditor,
                                               money_partnership=self, amount=amount)

    @property
    def can_do_annuity_payment(self):
        borrower_money = UserMoney.objects.get(user=self.borrower).balance
        return not self.annuity_payment_completed and borrower_money >= self.annuity_payment and self.is_started

    def can_do_dept_payment(self, amount):
        borrower_money = UserMoney.objects.get(user=self.borrower).balance
        return self.dept >= amount and borrower_money >= amount and self.is_started

    @property
    def next_annuity_payment(self):
        if self.last_annuity_payment:
            if self.last_annuity_payment < self.creation_time.date() + self.term:
                return self.last_annuity_payment + timedelta(days=1)
            else:
                return None
        else:
            return self.creation_time.date() + timedelta(days=1)

    @property
    def final_annuity_payment(self):
        return self.creation_time.date() + self.term

    def update_dept_if_necessary(self):
        if self.is_started and not self.annuity_payment_completed:
            today = date.today()
            yesterday = today - timedelta(days=1)
            annuity_payment = self.last_annuity_payment
            last_dept_day_included = self.last_dept_day_included
            if self.creation_time.date() < yesterday and (annuity_payment is None or annuity_payment < yesterday):
                if annuity_payment is None and last_dept_day_included is None:
                    start_date = self.creation_time.date() + timedelta(days=1)
                elif annuity_payment is None:
                    start_date = last_dept_day_included + timedelta(days=1)
                elif last_dept_day_included is None:
                    start_date = annuity_payment + timedelta(days=1)
                else:
                    if annuity_payment > last_dept_day_included:
                        start_date = annuity_payment + timedelta(days=1)
                    else:
                        start_date = last_dept_day_included + timedelta(days=1)
                dept_days = (date.today() - start_date).days
                self.dept += dept_days * settings.LATE_FEE_RATE * self.amount
                self.last_dept_day_included = yesterday
                self.save()

    def pay_for_annuity_payment(self):
        if self.can_do_annuity_payment:
            with transaction.atomic():
                self.update_dept_if_necessary()
                money_transaction = self.create_transaction(self.annuity_payment)
                money_transaction.execute()
                if self.last_annuity_payment is None:
                    self.last_annuity_payment = self.creation_time.date() + timedelta(days=1)
                else:
                    self.last_annuity_payment = self.last_annuity_payment + timedelta(days=1)
                if self.annuity_payment_completed and not self.has_dept:
                    self.status = self.FINISHED
                self.save()
                return money_transaction
        else:
            raise MoneyPartnershipException("Annuity payment can't be done")

    def pay_for_dept(self, amount):
        if self.can_do_dept_payment(amount):
            with transaction.atomic():
                self.update_dept_if_necessary()
                if self.dept < self.amount:
                    raise MoneyPartnershipException("Invalid amount on depth")
                money_transaction = self.create_transaction(amount)
                money_transaction.execute()
                self.dept -= amount
                if self.annuity_payment_completed and not self.has_dept:
                    self.status = self.FINISHED
                self.save()
                return money_transaction
        else:
            raise MoneyPartnershipException("Dept payment with amount {} can't be done")

    def to_return_on_cancel(self):
        days_left = self.term.days
        if self.last_annuity_payment is not None:
            days_left = (self.final_annuity_payment - self.last_annuity_payment).days
        return self.amount * days_left / self.term.days

    @property
    def can_be_cancelled(self):
        borrower_money = UserMoney.objects.get(user=self.borrower).balance
        return borrower_money >= self.to_return_on_cancel() and self.cancel_borrower_approved and self.cancel_creditor_approved

    def can_approve_cancel(self, user):
        if self.is_borrower(user):
            borrower_money = UserMoney.objects.get(user=self.borrower).balance
            return borrower_money >= self.to_return_on_cancel()
        else:
            return True

    def cancel(self):
        if self.can_be_cancelled:
            with transaction.atomic():
                money_transaction = self.create_transaction(self.to_return_on_cancel())
                money_transaction.execute()
                self.status = self.CANCELLED
                self.save()
        else:
            raise MoneyPartnershipException("Partnership can't be cancelled")

    def is_borrower(self, user):
        return self.borrower == user

    def is_creditor(self, user):
        return self.creditor == user

    def approve_cancel(self, user):
        if self.is_borrower(user):
            self.cancel_borrower_approved = True
        elif self.is_creditor(user):
            self.cancel_creditor_approved = True
        self.save()

    @property
    def cancel_initiated(self):
        return self.cancel_borrower_approved or self.cancel_creditor_approved


class MoneyRequestPartnership(MoneyPartnership):
    request = models.OneToOneField(MoneyRequestAd)
    suggestion = models.OneToOneField(MoneyRequestPartnershipSuggestion)

    @property
    def partnership_id(self):
        return self.moneypartnership_ptr.id

    @classmethod
    def can_be_concluded(cls, suggestion):
        creditor = suggestion.user
        return UserMoney.has_money(creditor, suggestion.request.amount)

    @classmethod
    def conclude(cls, suggestion):
        if cls.can_be_concluded(suggestion):
            with transaction.atomic():
                suggestion.accept()
                suggestion.request.close()
                if suggestion.from_proposal:
                    suggestion.from_proposal.close()
                request = suggestion.request
                annuity_payment = cls.get_annuity_payment(request.amount, suggestion.rate, request.term)
                partnership = cls.objects.create(borrower=request.user, creditor=suggestion.user, amount=request.amount,
                                                 annuity_payment=annuity_payment,
                                                 rate=suggestion.rate, term=request.term, request=request,
                                                 suggestion=suggestion)
                money_transaction = MoneyTransaction.objects.create(source_user=partnership.creditor,
                                                                    target_user=partnership.borrower,
                                                                    money_partnership=partnership,
                                                                    amount=partnership.amount)
                money_transaction.execute()
            return partnership
        else:
            raise MoneyPartnershipException("Can't conclude partnership")


class MoneyProposalPartnership(MoneyPartnership):
    proposal = models.OneToOneField(MoneyProposalAd)
    suggestion = models.OneToOneField(MoneyProposalPartnershipSuggestion)

    @property
    def partnership_id(self):
        return self.moneypartnership_ptr.id

    @classmethod
    def can_be_concluded(cls, suggestion):
        creditor = suggestion.proposal.user
        return UserMoney.has_money(creditor, suggestion.amount)

    @classmethod
    def conclude(cls, suggestion):
        if cls.can_be_concluded(suggestion):
            with transaction.atomic():
                suggestion.accept()
                suggestion.proposal.close()
                if suggestion.from_request:
                    suggestion.from_request.close()
                proposal = suggestion.proposal
                annuity_payment = cls.get_annuity_payment(suggestion.amount, proposal.rate, suggestion.term)
                partnership = cls.objects.create(borrower=suggestion.user, creditor=proposal.user,
                                                 amount=suggestion.amount,
                                                 annuity_payment=annuity_payment,
                                                 rate=proposal.rate, term=suggestion.term, proposal=proposal,
                                                 suggestion=suggestion)
                money_transaction = MoneyTransaction.objects.create(source_user=partnership.creditor,
                                                                    target_user=partnership.borrower,
                                                                    money_partnership=partnership,
                                                                    amount=partnership.amount)
                money_transaction.execute()
            return partnership
        else:
            raise MoneyPartnershipException("Can't conclude partnership")


class MoneyTransaction(models.Model):
    source_user = models.ForeignKey(User, related_name="source_user")
    target_user = models.ForeignKey(User, related_name="target_user")
    money_partnership = models.ForeignKey(MoneyPartnership)
    amount = MoneyField(max_digits=10, decimal_places=2, default=0)
    transaction_time = models.DateTimeField(auto_now_add=True)
    CREATED = "CRE"
    EXECUTED = "EXC"
    STATUS_CHOICES = (
        (CREATED, 'Created'),
        (EXECUTED, 'Executed')
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=CREATED)

    def execute(self):
        source_user_money = UserMoney.objects.get(user=self.source_user)
        target_user_money = UserMoney.objects.get(user=self.target_user)
        with transaction.atomic():
            source_user_money.withdraw_money(self.amount)
            target_user_money.put_money(self.amount)
            self.status = self.EXECUTED
            self.save()
