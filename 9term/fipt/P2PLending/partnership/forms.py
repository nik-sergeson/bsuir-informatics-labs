from django import forms
from django.conf import settings
from django.forms import ModelForm, widgets
from djmoney.forms.fields import MoneyField

from P2PLending.partnership.models import MoneyRequestPartnershipSuggestion, MoneyProposalPartnershipSuggestion

TERM_CHOICES = getattr(settings, 'DEFAULT_CREDIT_TERMS', [('', 'Never'), ])


class MoneyRequestPartnSuggestionForm(ModelForm):
    class Meta:
        model = MoneyRequestPartnershipSuggestion
        fields = ['rate']


class MoneyProposalPartnSuggestionForm(ModelForm):
    term = forms.DurationField(widget=widgets.Select(choices=TERM_CHOICES))

    class Meta:
        model = MoneyProposalPartnershipSuggestion
        fields = ['amount', 'term']


class AmountForm(forms.Form):
    amount = MoneyField()
