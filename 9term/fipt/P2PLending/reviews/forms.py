from django.forms import ModelForm
from P2PLending.reviews.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']
