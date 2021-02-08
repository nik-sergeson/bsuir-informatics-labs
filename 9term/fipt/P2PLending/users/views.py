from braces.views import CsrfExemptMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import render, redirect, reverse

from P2PLending.reviews.forms import ReviewForm
from P2PLending.reviews.models import Review
from P2PLending.users.forms import ProfileForm
from P2PLending.users.models import User


class ProfileView(CsrfExemptMixin, LoginRequiredMixin, View):
    def get(self, request):
        context = {"form": ProfileForm}
        return render(request, "profile/user_profile.html", context)

    def post(self, request):
        user = request.user
        user.home_ownership = request.POST.get("home_ownership")
        user.income = request.POST.get("annual_income")
        user.save()
        return redirect(reverse("user_info", kwargs={"user_id": user.id}))


class UserInfoView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        context = {"profile_owner": user,
                   "review_form": ReviewForm,
                   "review_list": Review.objects.filter(reviewed_user=user)
                   }
        return render(request, "profile/user_info.html", context)
