from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from P2PLending.lending.models import MoneyProposalAd, MoneyRequestAd
from P2PLending.lending.signals import proposal_closed, request_closed
from P2PLending.partnership.models import MoneyRequestPartnershipSuggestion, MoneyProposalPartnershipSuggestion


@receiver(post_save, sender=MoneyRequestPartnershipSuggestion)
def validate_request_suggestion(sender, instance, created, **kwargs):
    if created:
        instance.validate()


@receiver(post_save, sender=MoneyProposalPartnershipSuggestion)
def validate_proposal_suggestion(sender, instance, created, **kwargs):
    if created:
        instance.validate()


@receiver(proposal_closed, sender=MoneyProposalAd)
def proposal_close_listener(sender, proposal, **kwargs):
    with transaction.atomic():
        for req_suggestion in MoneyRequestPartnershipSuggestion.objects.filter(from_proposal=proposal):
            req_suggestion.cancel()


@receiver(request_closed, sender=MoneyRequestAd)
def request_close_listener(sender, request, **kwargs):
    with transaction.atomic():
        for prop_suggestion in MoneyProposalPartnershipSuggestion.objects.filter(from_request=request):
            prop_suggestion.cancel()
