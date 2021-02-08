from django.conf.urls import url

from P2PLending.partnership.api import RequestSuggestionAPI, ProposalSuggestionAPI, ProposalPartnershipSuggestionsAPI, \
    RequestPartnershipSuggestionsAPI, UserProposalsToRequestAPI, UserRequestsToProposalAPI
from P2PLending.partnership.views import RequestPartnershipSuggestionView, ProposalPartnershipSuggestionView, \
    RequestPartnershipView, ProposalPartnershipView, RequestPartnershipListView, ProposalPartnershipListView, \
    AnnuityPaymentView, TransactionView, DeptPaymentView, ProposalToSuggestionView, RequestToSuggestionView

urlpatterns = [
    url(r'^request/(?P<request_id>\d+)/suggestion$', RequestPartnershipSuggestionView.as_view(),
        name="request_partnership_suggestion"),
    url(r'^proposal/(?P<proposal_id>\d+)/suggestion$', ProposalPartnershipSuggestionView.as_view(),
        name="proposal_partnership_suggestion"),
    url(r'^request-partnership/(?P<partnership_id>\d+)$', RequestPartnershipView.as_view(), name="request_partnership"),
    url(r'^proposal-partnership/(?P<partnership_id>\d+)$', ProposalPartnershipView.as_view(),
        name="proposal_partnership"),
    url(r'^request-partnerships/(?P<page>\d+)$', RequestPartnershipListView.as_view(), name="request_partnership_list"),
    url(r'^proposal-partnerships/(?P<page>\d+)$', ProposalPartnershipListView.as_view(),
        name="proposal_partnership_list"),
    url(r'^request/(?P<request_id>\d*)/proposal/(?P<proposal_id>\d*)/to_suggestion$',
        ProposalToSuggestionView.as_view(), name="proposal_to_suggestion"),
    url(r'^proposal/(?P<proposal_id>\d*)/request/(?P<request_id>\d*)/to_suggestion$', RequestToSuggestionView.as_view(),
        name="request_to_suggestion"),
    url(r'^payment/annuity/(?P<partnership_id>\d*)/$', AnnuityPaymentView.as_view(),
        name="annuity_payment"),
    url(r'^payment/dept/(?P<partnership_id>\d*)/$', DeptPaymentView.as_view(),
        name="dept_payment"),
    url(r'^transaction/(?P<transaction_id>\d*)/$', TransactionView.as_view(), name="transaction"),
    url(r'^api/request-suggestion/(?P<suggestion_id>\d*)$', RequestSuggestionAPI.as_view(),
        name="api_request_suggestion"),
    url(r'^api/proposal-suggestion/(?P<suggestion_id>\d*)$', ProposalSuggestionAPI.as_view(),
        name="api_proposal_suggestion"),
    url(r'^api/request/(?P<request_id>\d*)/suggestions$', RequestPartnershipSuggestionsAPI.as_view(),
        name="api_request_suggestions"),
    url(r'^api/proposal/(?P<proposal_id>\d*)/suggestions$', ProposalPartnershipSuggestionsAPI.as_view(),
        name="api_proposal_suggestions"),
    url(r'^api/request/(?P<request_id>\d*)/user_proposals$', UserProposalsToRequestAPI.as_view(),
        name="api_user_proposals_to_request"),
    url(r'^api/proposal/(?P<proposal_id>\d*)/user_requests', UserRequestsToProposalAPI.as_view(),
        name="api_user_requests_to_proposal"),
]
