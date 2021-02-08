from django.conf.urls import url

from P2PLending.lending.api import RequestRecommendationsAPI, ProposalRecommendationsAPI
from P2PLending.lending.views import ProposalView, ProposalListView, RequestView, RequestListView

urlpatterns = [
    url(r'^proposal/(?P<proposal_id>\d*)$', ProposalView.as_view(), name="proposal"),
    url(r'^proposal$', ProposalView.as_view(), name="proposal"),
    url(r'^proposals/(?P<page>\d+)$', ProposalListView.as_view(), name="proposals"),
    url(r'^request/(?P<request_id>\d*)$', RequestView.as_view(), name="request"),
    url(r'^request$', RequestView.as_view(), name="request"),
    url(r'^requests/(?P<page>\d+)$', RequestListView.as_view(), name="requests"),
    url(r'^api/proposal/(?P<proposal_id>\d*)/recommendations$', ProposalRecommendationsAPI.as_view(),
        name="api_proposal_recommendations"),
    url(r'^api/request/(?P<request_id>\d*)/recommendations$', RequestRecommendationsAPI.as_view(),
        name="api_request_recommendations"),
]
