from P2PLending.lending.models import MoneyRequestAd, MoneyProposalAd, Recommendation
from rest_framework.serializers import ModelSerializer


class RequestAdSerializer(ModelSerializer):
    class Meta:
        model = MoneyRequestAd
        fields = ('end', 'creation_date', 'user', 'amount', 'term', 'return_probability')


class ProposalAdSerializer(ModelSerializer):
    class Meta:
        model = MoneyProposalAd
        fields = ('min_amount', 'max_amount', 'min_term', 'max_term', 'end', 'creation_date', 'user', 'rate')


class ProposalRecommendationSerializer(ModelSerializer):
    request = RequestAdSerializer()

    class Meta:
        model = Recommendation
        fields = ('similarity', 'request')


class RequestRecommendationSerializer(ModelSerializer):
    proposal = ProposalAdSerializer()

    class Meta:
        model = Recommendation
        fields = ('similarity', 'proposal')
