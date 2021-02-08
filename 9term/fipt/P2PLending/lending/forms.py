from datetimewidget.widgets import DateWidget
from django import forms
from django.forms import ModelForm, widgets
from django.conf import settings
from P2PLending.lending.models import MoneyProposalAd, MoneyRequestAd

TERM_CHOICES = getattr(settings, 'DEFAULT_CREDIT_TERMS', [('', 'Never'), ])


class MoneyRequestForm(ModelForm):
    end = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    term = forms.DurationField(widget=widgets.Select(choices=TERM_CHOICES))

    class Meta:
        model = MoneyRequestAd
        fields = ['amount', 'term', 'end']


class MoneyProposalForm(ModelForm):
    min_term = forms.DurationField(widget=widgets.Select(choices=TERM_CHOICES))
    max_term = forms.DurationField(widget=widgets.Select(choices=TERM_CHOICES))
    end = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))

    class Meta:
        model = MoneyProposalAd
        fields = ['min_amount', 'max_amount', 'rate', 'min_term', 'max_term', 'end']
