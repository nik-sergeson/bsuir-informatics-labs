from rest_framework.generics import ListAPIView

from P2PLending.lending.models import Recommendation
from P2PLending.lending.serializers import RequestRecommendationSerializer, ProposalRecommendationSerializer


class RequestRecommendationsAPI(ListAPIView):
    serializer_class = RequestRecommendationSerializer

    def get_queryset(self):
        request_id = self.kwargs['request_id']
        return Recommendation.objects.filter(request__id=request_id)


class ProposalRecommendationsAPI(ListAPIView):
    serializer_class = ProposalRecommendationSerializer

    def get_queryset(self):
        proposal_id = self.kwargs['proposal_id']
        return Recommendation.objects.filter(proposal__id=proposal_id)
