from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from P2PLending.lending.models import MoneyProposalAd, MoneyRequestAd
from P2PLending.lending.recomemndations import get_requests_similar_to_proposal, get_proposals_similar_to_request
from P2PLending.lending.serializers import RequestAdSerializer, ProposalAdSerializer
from P2PLending.partnership.models import MoneyProposalPartnershipSuggestion, MoneyRequestPartnershipSuggestion, MoneyRequestPartnership, MoneyProposalPartnership
from P2PLending.partnership.serializers import RequestPartnershipSuggestionSerializer, \
    ProposalPartnershipSuggestionSerializer


class ProposalSuggestionAPI(APIView):
    def get(self, request, suggestion_id):
        suggestion = MoneyProposalPartnershipSuggestion.objects.get(id=suggestion_id)
        MoneyProposalPartnership.conclude(suggestion)
        return Response()

    def delete(self, request, suggestion_id):
        suggestion = MoneyProposalPartnershipSuggestion.objects.get(id=suggestion_id)
        suggestion.reject()
        return Response()


class RequestSuggestionAPI(APIView):
    def get(self, request, suggestion_id):
        suggestion = MoneyRequestPartnershipSuggestion.objects.get(id=suggestion_id)
        MoneyRequestPartnership.conclude(suggestion)
        return Response()

    def delete(self, request, suggestion_id):
        suggestion = MoneyRequestPartnershipSuggestion.objects.get(id=suggestion_id)
        suggestion.reject()
        return Response()


class RequestPartnershipSuggestionsAPI(ListAPIView):
    serializer_class = RequestPartnershipSuggestionSerializer

    def get_queryset(self):
        request_id = self.kwargs['request_id']
        return MoneyRequestPartnershipSuggestion.objects.filter(request__id=request_id)


class ProposalPartnershipSuggestionsAPI(ListAPIView):
    serializer_class = ProposalPartnershipSuggestionSerializer

    def get_queryset(self):
        proposal_id = self.kwargs['proposal_id']
        return MoneyProposalPartnershipSuggestion.objects.filter(proposal__id=proposal_id)


class UserRequestsToProposalAPI(ListAPIView):
    serializer_class = RequestAdSerializer

    def get_queryset(self):
        user = self.request.user
        proposal_id = self.kwargs['proposal_id']
        proposal = MoneyProposalAd.objects.get(id=proposal_id)
        return get_requests_similar_to_proposal(proposal, user=user).filter(
            moneyrequestpartnershipsuggestion__isnull=True)


class UserProposalsToRequestAPI(ListAPIView):
    serializer_class = ProposalAdSerializer

    def get_queryset(self):
        user = self.request.user
        request_id = self.kwargs['request_id']
        request = MoneyRequestAd.objects.get(id=request_id)
        return get_proposals_similar_to_request(request, user=user).filter(
            moneyproposalpartnershipsuggestion__isnull=True)
