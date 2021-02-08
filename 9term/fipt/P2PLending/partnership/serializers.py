from P2PLending.partnership.models import MoneyRequestPartnershipSuggestion, MoneyProposalPartnershipSuggestion
from rest_framework.serializers import ModelSerializer


class RequestPartnershipSuggestionSerializer(ModelSerializer):
    class Meta:
        model = MoneyRequestPartnershipSuggestion
        fields = ('creation_date', 'user', 'rate')


class ProposalPartnershipSuggestionSerializer(ModelSerializer):
    class Meta:
        model = MoneyProposalPartnershipSuggestion
        fields = ('creation_date', 'user', 'amount', 'term', 'return_probability')
