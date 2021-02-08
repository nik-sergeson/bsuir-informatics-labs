from django.conf.urls import url

from P2PLending.users.views import ProfileView, UserInfoView

urlpatterns = [
    url(r'^profile$', ProfileView.as_view(), name="profile"),
    url(r'^user_info/(?P<user_id>\d+)$', UserInfoView.as_view(), name="user_info"),
]