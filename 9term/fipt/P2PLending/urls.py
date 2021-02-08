"""P2PLending URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from registration.backends.default.views import RegistrationView

from P2PLending.lending.views import IndexView, AboutView
from P2PLending.users.forms import UserRegistrationForm
from P2PLending.users.views import ProfileView, UserInfoView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register$', RegistrationView.as_view(form_class=UserRegistrationForm), name="registration_register"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^profile$', ProfileView.as_view(), name="profile"),
    url(r'^user_info/(?P<user_id>\d+)$', UserInfoView.as_view(), name="user_info"),
    url(r'^lending/', include('P2PLending.lending.urls')),
    url(r'^partnership/', include('P2PLending.partnership.urls')),
    url(r'^user/', include('P2PLending.users.urls')),
    url(r'^paypal/', include('P2PLending.paypal.urls', namespace="paypal")),
    url(r'^reviews/', include('P2PLending.reviews.urls')),
    url(r'^about$', AboutView.as_view(), name="about")

]
