from django.conf.urls import url

from P2PLending.paypal.views import *

urlpatterns = [
    url(r'^put/(?P<user_id>\d+)/$', PutMoneyView.as_view(), name="put"),
    url(r'^proceed/(?P<user_id>\d+)/$', ProceedPutMoneyView.as_view(), name="proceed"),
    url(r'^cancel/(?P<user_id>\d+)/$', CancelPutMoneyView.as_view(), name="cancel"),
    url(r'^withdraw/(?P<user_id>\d+)/$', WithdrawMoneyView.as_view(), name="withdraw"),
]
