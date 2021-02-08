from django.db.models.signals import post_save
from django.dispatch import receiver

from P2PLending.lending.models import MoneyRequestAd, MoneyProposalAd, Recommendation
from P2PLending.lending.raiting import update_user_requests_return_prob
from P2PLending.lending.recomemndations import update_proposal_recommendations, update_request_recommendations
from P2PLending.lending.signals import proposal_closed, request_closed
from P2PLending.users.models import User


@receiver(post_save, sender=MoneyRequestAd)
def request_ad_create_listener(sender, instance, created, **kwargs):
    if created:
        update_request_recommendations(instance)


@receiver(post_save, sender=MoneyProposalAd)
def proposal_ad_create_listener(sender, instance, created, **kwargs):
    if created:
        update_proposal_recommendations(instance)


@receiver(post_save, sender=User)
def user_update_listener(sender, instance, created, **kwargs):
    if not created:
        update_user_requests_return_prob(instance)


@receiver(request_closed, sender=MoneyRequestAd)
def handle_request_closed(sender, request, **kwargs):
    Recommendation.remove(request=request)


@receiver(proposal_closed, sender=MoneyProposalAd)
def handle_proposal_close(sender, proposal, **kwargs):
    Recommendation.remove(proposal=proposal)
