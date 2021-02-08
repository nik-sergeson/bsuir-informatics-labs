import math
import numpy
from datetime import date, timedelta
from django.conf import settings
from django.db import transaction

from P2PLending.lending.models import MoneyProposalAd, MoneyRequestAd, Recommendation


def get_similarity(proposal, request):
    if proposal is None or request is None:
        return None
    angle = 0
    max_term_delta = timedelta(days=settings.MAX_CREDIT_TERM - settings.MIN_CREDIT_TERM).total_seconds()
    max_amount_delta = settings.MAX_CREDIT_AMOUNT - settings.MIN_CREDIT_AMOUNT
    if not proposal.min_term <= request.term <= proposal.max_term:
        if abs(request.term.total_seconds() - proposal.min_term.total_seconds()) < abs(
                        request.term.total_seconds() - proposal.max_term.total_seconds()):
            angle += abs(request.term.total_seconds() - proposal.min_term.total_seconds()) * 90 / max_term_delta
        else:
            angle += abs(request.term.total_seconds() - proposal.max_term.total_seconds()) * 90 / max_term_delta
    if not proposal.min_amount <= request.amount <= proposal.max_amount:
        if abs(request.amount.amount - proposal.min_amount.amount) < abs(
                        request.amount.amount - proposal.max_amount.amount):
            angle += float(abs(request.amount.amount - proposal.min_amount.amount)) * 90 / max_amount_delta
        else:
            angle += float(abs(request.amount.amount - proposal.max_amount.amount)) * 90 / max_amount_delta
    theta = (angle / 180.) * numpy.pi
    return (1 + math.cos(theta)) / 2


def update_request_recommendations(request):
    with transaction.atomic():
        proposals = MoneyProposalAd.objects.all().exclude(user=request.user, end__gte=date.today())
        for proposal in proposals:
            similarity = get_similarity(proposal, request)
            Recommendation.objects.create(request=request, proposal=proposal, similarity=similarity)


def update_proposal_recommendations(proposal):
    with transaction.atomic():
        requests = MoneyRequestAd.objects.all().exclude(user=proposal.user, end__gte=date.today())
        for request in requests:
            similarity = get_similarity(proposal, request)
            Recommendation.objects.create(request=request, proposal=proposal, similarity=similarity)


def get_requests_similar_to_proposal(proposal, **kwargs):
    return MoneyRequestAd.get(amount__gte=proposal.min_amount, amount__lte=proposal.max_amount,
                              term__gte=proposal.min_term, term__lte=proposal.max_term, **kwargs)


def get_proposals_similar_to_request(request, **kwargs):
    return MoneyProposalAd.get(min_amount__lte=request.amount, max_amount__gte=request.amount,
                               min_term__lte=request.term, max_term__gte=request.term, **kwargs)
