import datetime
from django.db import models, transaction
from djmoney.models.fields import MoneyField
from P2PLending.lending.signals import request_closed, proposal_closed
from P2PLending.users.models import User


class AdvertisementStatus(models.Model):
    OPENED = "OPN"
    CLOSED = "CLS"
    STATUS_CHOICES = (
        (OPENED, 'Opened'),
        (CLOSED, 'Closed')
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=OPENED)

    class Meta:
        abstract = True

    def close(self):
        self.status = self.CLOSED
        self.save()

    @property
    def is_opened(self):
        return self.status == self.OPENED

    @property
    def is_closed(self):
        return self.status == self.CLOSED


class MoneyRequest(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    amount = MoneyField(max_digits=10, decimal_places=2)
    term = models.DurationField()
    return_probability = models.FloatField(null=True)

    class Meta:
        abstract = True

    def is_owner(self, user):
        return self.user == user

    @classmethod
    def get_for_user(cls, user):
        return cls.objects.filter(user=user)


class MoneyRequestAd(MoneyRequest, AdvertisementStatus):
    end = models.DateField()

    @property
    def is_opened(self):
        if self.end < datetime.date.today():
            self.close()
        return super().is_opened

    @property
    def is_closed(self):
        if self.end < datetime.date.today():
            self.close()
        return super().is_closed

    def close(self):
        super().close()
        request_closed.send(sender=MoneyRequestAd, request=self)

    @classmethod
    def get_all(cls):
        return list(filter(lambda x: x.is_opened, cls.objects.all()))

    @classmethod
    def get(cls, **kwargs):
        return list(filter(lambda x: x.is_opened, cls.objects.filter(**kwargs)))


class MoneyProposal(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    rate = models.FloatField()

    class Meta:
        abstract = True

    def is_owner(self, user):
        return self.user == user

    @classmethod
    def get_for_user(cls, user):
        return cls.objects.filter(user=user)


class MoneyProposalAd(MoneyProposal, AdvertisementStatus):
    min_amount = MoneyField(max_digits=10, decimal_places=2)
    max_amount = MoneyField(max_digits=10, decimal_places=2)
    min_term = models.DurationField()
    max_term = models.DurationField()
    end = models.DateField()

    @property
    def is_opened(self):
        if self.end < datetime.date.today():
            self.close()
        return super().is_opened

    @property
    def is_closed(self):
        if self.end < datetime.date.today():
            self.close()
        return super().is_closed

    def close(self):
        super().close()
        proposal_closed.send(sender=MoneyProposalAd, proposal=self)

    @classmethod
    def get_all(cls):
        return list(filter(lambda x: x.is_opened, cls.objects.all()))

    @classmethod
    def get(cls, **kwargs):
        return list(filter(lambda x: x.is_opened, cls.objects.filter(**kwargs)))


class Recommendation(models.Model):
    request = models.ForeignKey(MoneyRequestAd)
    proposal = models.ForeignKey(MoneyProposalAd)
    similarity = models.FloatField()

    @classmethod
    def remove(cls, proposal=None, request=None):
        with transaction.atomic():
            if request:
                cls.objects.filter(request=request).delete()
            if proposal:
                cls.objects.filter(proposal=proposal).delete()
