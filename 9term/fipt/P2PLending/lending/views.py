# -*- coding: utf-8 -*-
from datetime import datetime

from braces.views import CsrfExemptMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic.list import ListView

from P2PLending.lending.forms import MoneyRequestForm, MoneyProposalForm
from P2PLending.lending.models import MoneyRequestAd, MoneyProposalAd, Recommendation
from P2PLending.lending.raiting import get_request_return_prob
from P2PLending.lending.recomemndations import get_proposals_similar_to_request, get_requests_similar_to_proposal
from P2PLending.partnership.forms import MoneyProposalPartnSuggestionForm, MoneyRequestPartnSuggestionForm
from P2PLending.partnership.models import MoneyRequestPartnershipSuggestion, MoneyProposalPartnershipSuggestion, \
    MoneyRequestPartnership, MoneyProposalPartnership
from P2PLending.partnership.utils import proposal_in_partnership, request_in_partnership


class IndexView(CsrfExemptMixin, View):
    def get(self, request):
        context = {
            'title': 'Главная',
            'year': datetime.now().year,
        }
        return render(request, "index.html", context)


class ProposalListView(LoginRequiredMixin, ListView):
    model = MoneyProposalAd
    template_name = "lending/proposal_list.html"
    context_object_name = "proposal_list"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MoneyProposalForm
        return context

    def get_queryset(self):
        return self.model.get_all()


class RequestListView(LoginRequiredMixin, ListView):
    model = MoneyRequestAd
    template_name = "lending/request_list.html"
    context_object_name = "request_list"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MoneyRequestForm
        return context

    def get_queryset(self):
        return self.model.get_all()


class ProposalView(LoginRequiredMixin, View):
    def get(self, request, proposal_id):
        proposal = get_object_or_404(MoneyProposalAd, pk=proposal_id)
        is_owner = proposal.is_owner(request.user)
        context = {"money_proposal": proposal, "is_owner": is_owner,
                   "in_partnership": proposal_in_partnership(proposal)}
        if is_owner:
            suggestions = MoneyProposalPartnershipSuggestion.get_for_proposal(proposal=proposal)
            context["suggestions"] = suggestions
            context["recommendations"] = [{"request": rec.request, "similarity": rec.similarity} for rec in
                                          Recommendation.objects.filter(proposal=proposal).exclude(
                                              request__user=request.user)]
        else:
            suggestions = MoneyProposalPartnershipSuggestion.objects.filter(proposal=proposal, user=request.user)
            context["suggestions"] = suggestions
            context["suggestion_form"] = MoneyProposalPartnSuggestionForm
            user_requests = get_requests_similar_to_proposal(proposal, user=request.user)
            user_requests = filter(
                lambda user_request: not MoneyProposalPartnershipSuggestion.objects.filter(proposal=proposal,
                                                                                           from_request=user_request).exists(),
                user_requests)
            context["user_requests"] = list(user_requests)
        return render(request, "lending/proposal.html", context)

    def post(self, request, proposal_id=None):
        form = MoneyProposalForm(request.POST)
        user = request.user
        if form.is_valid():
            money_proposal = form.save(commit=False)
            money_proposal.user = user
            money_proposal.save()
            return redirect(reverse("proposal", kwargs={"proposal_id": money_proposal.id}))
        else:
            context = {"form": form,
                       "back_url": request.path}
            return render(request, "form_errors.html", context)


class RequestView(LoginRequiredMixin, View):
    def get(self, request, request_id):
        money_request = get_object_or_404(MoneyRequestAd, pk=request_id)
        is_owner = money_request.is_owner(request.user)
        context = {"money_request": money_request, "is_owner": is_owner,
                   "in_partnership": request_in_partnership(money_request)}
        if is_owner:
            suggestions = MoneyRequestPartnershipSuggestion.get_for_request(request=money_request)
            context["suggestions"] = suggestions
            context["recommendations"] = [{"proposal": rec.proposal, "similarity": rec.similarity} for rec in
                                          Recommendation.objects.filter(request=money_request).exclude(
                                              proposal__user=request.user)]
        else:
            suggestions = MoneyRequestPartnershipSuggestion.objects.filter(request=money_request, user=request.user)
            context["suggestions"] = suggestions
            context["suggestion_form"] = MoneyRequestPartnSuggestionForm
            user_proposals = get_proposals_similar_to_request(money_request, user=request.user)
            user_proposals = filter(
                lambda user_proposal: not MoneyRequestPartnershipSuggestion.objects.filter(request=money_request,
                                                                                           from_proposal=user_proposal), user_proposals)
            context["user_proposals"] = list(user_proposals)
        return render(request, "lending/request.html", context)

    def post(self, request, request_id=None):
        user = request.user
        form = MoneyRequestForm(request.POST)
        if form.is_valid():
            money_request = form.save(commit=False)
            money_request.user = user
            money_request.return_probability = get_request_return_prob(user, money_request)
            money_request.save()
            return redirect(reverse("request", kwargs={"request_id": money_request.id}))
        else:
            context = {"form": form,
                       "back_url": request.path}
            return render(request, "form_errors.html", context)


class AboutView(View):
    def get(self, request):
        context = {
            'title': 'О сервисе',
        }
        return render(request, "about.html", context)
