from braces.views import CsrfExemptMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic.list import ListView

from P2PLending.partnership.forms import MoneyProposalPartnSuggestionForm, \
    MoneyRequestPartnSuggestionForm, AmountForm
from P2PLending.partnership.models import MoneyRequestAd, MoneyProposalAd, MoneyRequestPartnershipSuggestion, \
    MoneyProposalPartnershipSuggestion, MoneyProposalPartnership, MoneyRequestPartnership, MoneyTransaction, \
    MoneyPartnership


class RequestPartnershipSuggestionView(CsrfExemptMixin, LoginRequiredMixin, View):
    def post(self, request, request_id):
        target_request = get_object_or_404(MoneyRequestAd, pk=request_id)
        partnership_form = MoneyRequestPartnSuggestionForm(request.POST)
        if partnership_form.is_valid():
            partn_suggestion = partnership_form.save(commit=False)
            partn_suggestion.user = request.user
            partn_suggestion.request = target_request
            partn_suggestion.save()
            return redirect(reverse("request", kwargs={"request_id": request_id}))
        else:
            context = {"form": partnership_form,
                       "back_url": request.path}
            return render(request, "form_errors.html", context)


class ProposalPartnershipSuggestionView(CsrfExemptMixin, LoginRequiredMixin, View):
    def post(self, request, proposal_id):
        target_proposal = get_object_or_404(MoneyProposalAd, pk=proposal_id)
        partnership_form = MoneyProposalPartnSuggestionForm(request.POST)
        if partnership_form.is_valid():
            partn_suggestion = partnership_form.save(commit=False)
            partn_suggestion.user = request.user
            partn_suggestion.proposal = target_proposal
            partn_suggestion.save()
            return redirect(reverse("proposal", kwargs={"proposal_id": proposal_id}))
        else:
            context = {"form": partnership_form,
                       "back_url": request.path}
            return render(request, "form_errors.html", context)


class ProposalPartnershipView(LoginRequiredMixin, View):
    def get(self, request, partnership_id):
        prop_partnership = get_object_or_404(MoneyProposalPartnership, pk=partnership_id)
        if not prop_partnership.is_borrower(request.user) and not prop_partnership.is_creditor(request.user):
            raise PermissionDenied
        context = self.get_context_data(prop_partnership)
        return render(request, "partnership/proposal_partnership.html", context=context)

    def post(self, request, partnership_id):
        prop_partnership = get_object_or_404(MoneyProposalPartnership, pk=partnership_id)
        if not prop_partnership.is_borrower(request.user) and not prop_partnership.is_creditor(request.user):
            raise PermissionDenied
        prop_partnership.approve_cancel(request.user)
        if prop_partnership.can_be_cancelled:
            prop_partnership.cancel()
        context = self.get_context_data(prop_partnership)
        return render(request, "partnership/proposal_partnership.html", context=context)

    def get_context_data(self, prop_partnership):
        return {
            "partnership": prop_partnership,
            "is_borrower": prop_partnership.is_borrower(self.request.user),
            "dept_form": AmountForm,
            "can_approve_cancel": prop_partnership.can_approve_cancel(self.request.user),
            "approved_cancel": (prop_partnership.is_borrower(
                self.request.user) and prop_partnership.cancel_borrower_approved) or (prop_partnership.is_creditor(
                self.request.user) and prop_partnership.cancel_creditor_approved),
        }


class RequestPartnershipView(LoginRequiredMixin, View):
    def get(self, request, partnership_id):
        req_partnership = get_object_or_404(MoneyRequestPartnership, pk=partnership_id)
        if not req_partnership.is_borrower(request.user) and not req_partnership.is_creditor(request.user):
            raise PermissionDenied
        context = self.get_context_data(req_partnership)
        return render(request, "partnership/request_partnership.html", context=context)

    def post(self, request, partnership_id):
        req_partnership = get_object_or_404(MoneyRequestPartnership, pk=partnership_id)
        if not req_partnership.is_borrower(request.user) and not req_partnership.is_creditor(request.user):
            raise PermissionDenied
        req_partnership.approve_cancel(request.user)
        if req_partnership.can_be_cancelled:
            req_partnership.cancel()
        context = self.get_context_data(req_partnership)
        return render(request, "partnership/request_partnership.html", context=context)

    def get_context_data(self, req_partnership):
        return {"partnership": req_partnership,
                "is_borrower": req_partnership.is_borrower(self.request.user),
                "dept_form": AmountForm,
                "can_approve_cancel": req_partnership.can_approve_cancel(self.request.user),
                "approved_cancel": (req_partnership.is_borrower(
                    self.request.user) and req_partnership.cancel_borrower_approved) or (req_partnership.is_creditor(
                    self.request.user) and req_partnership.cancel_creditor_approved),
                }


class RequestPartnershipListView(LoginRequiredMixin, ListView):
    model = MoneyRequestPartnership
    template_name = "partnership/request_partnership_list.html"
    context_object_name = "partnership_list"
    paginate_by = 25

    def get_queryset(self):
        return MoneyRequestPartnership.objects.filter(
            Q(request__user=self.request.user) | Q(suggestion__user=self.request.user))


class ProposalPartnershipListView(LoginRequiredMixin, ListView):
    model = MoneyProposalPartnership
    template_name = "partnership/proposal_partnership_list.html"
    context_object_name = "partnership_list"
    paginate_by = 25

    def get_queryset(self):
        return MoneyProposalPartnership.objects.filter(
            Q(proposal__user=self.request.user) | Q(suggestion__user=self.request.user))


class AnnuityPaymentView(LoginRequiredMixin, View):
    def post(self, request, partnership_id):
        partnership = get_object_or_404(MoneyPartnership, pk=partnership_id)
        if partnership.can_do_annuity_payment:
            transaction = partnership.pay_for_annuity_payment()
            return redirect(reverse("transaction", kwargs={"transaction_id": transaction.id}))


class DeptPaymentView(LoginRequiredMixin, View):
    def post(self, request, partnership_id):
        partnership = get_object_or_404(MoneyPartnership, pk=partnership_id)
        form = AmountForm(request.POST)
        if form.is_valid() and partnership.can_do_dept_payment(form.cleaned_data['amount']):
            transaction = partnership.pay_for_dept(form.cleaned_data['amount'])
            return redirect(reverse("transaction", kwargs={"transaction_id": transaction.id}))
        else:
            context = {"form": form,
                       "back_url": request.path}
            return render(request, "form_errors.html", context)


class TransactionView(LoginRequiredMixin, View):
    def get(self, request, transaction_id):
        transaction = get_object_or_404(MoneyTransaction, pk=transaction_id)
        if request.user != transaction.source_user and request.user != transaction.target_user:
            raise PermissionDenied
        context = {"transaction": transaction}
        return render(request, "transaction/transaction.html", context)


class RequestToSuggestionView(LoginRequiredMixin, View):
    def post(self, request, proposal_id, request_id):
        money_request = get_object_or_404(MoneyRequestAd, pk=request_id)
        money_proposal = get_object_or_404(MoneyProposalAd, pk=proposal_id)
        MoneyProposalPartnershipSuggestion.objects.create(proposal=money_proposal, user=money_request.user,
                                                          amount=money_request.amount, term=money_request.term,
                                                          from_request=money_request)
        return redirect(reverse("proposal", kwargs={"proposal_id": proposal_id}))


class ProposalToSuggestionView(LoginRequiredMixin, View):
    def post(self, request, request_id, proposal_id):
        money_request = get_object_or_404(MoneyRequestAd, pk=request_id)
        money_proposal = get_object_or_404(MoneyProposalAd, pk=proposal_id)
        MoneyRequestPartnershipSuggestion.objects.create(request=money_request, user=money_proposal.user,
                                                         rate=money_proposal.rate, from_proposal=money_proposal)
        return redirect(reverse("request", kwargs={"request_id": request_id}))
