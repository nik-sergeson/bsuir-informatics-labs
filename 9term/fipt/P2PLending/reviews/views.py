from braces.views import CsrfExemptMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.views import View
from P2PLending.reviews.forms import ReviewForm
from P2PLending.users.models import User


class ReviewView(CsrfExemptMixin, LoginRequiredMixin, View):
    def post(self, request, reviewed_id):
        review_form = ReviewForm(request.POST)
        author = request.user
        reviewed_user = get_object_or_404(User, pk=reviewed_id)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = author
            review.reviewed_user = reviewed_user
            review.save()
            return redirect(reverse("user_info", kwargs={"user_id": reviewed_id}))
        else:
            context = {"form": review_form,
                       "back_url": request.path}
            return render(request, "form_errors.html", context)
