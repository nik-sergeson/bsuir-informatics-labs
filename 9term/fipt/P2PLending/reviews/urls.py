from django.conf.urls import url
from P2PLending.reviews.views import ReviewView

urlpatterns = [
    url(r'^create/(?P<reviewed_id>\d*)$', ReviewView.as_view(), name="create_review"),
]
