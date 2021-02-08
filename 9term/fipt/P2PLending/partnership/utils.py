from P2PLending.partnership.models import MoneyRequestPartnership, MoneyProposalPartnership


def request_in_partnership(request):
    return MoneyRequestPartnership.objects.filter(request=request).exists()


def proposal_in_partnership(proposal):
    return MoneyProposalPartnership.objects.filter(proposal=proposal).exists()
