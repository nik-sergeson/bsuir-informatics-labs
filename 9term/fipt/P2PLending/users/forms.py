from django import forms
from django.contrib.auth import get_user_model
from P2PLending.users.models import User, UserMoney
from registration.forms import RegistrationForm


class UserRegistrationForm(RegistrationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField()
    phone = forms.CharField()
    birth_date = forms.DateField()

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "patronymic", "phone", "birth_date"]

class ProfileForm(forms.Form):
    home_ownership = forms.ChoiceField(widget=forms.widgets.RadioSelect, choices=User.HOME_OWNERSHIP)
    annual_income = forms.IntegerField()

    class Meta:
        model = User
        fields = ["home_ownership", "income"]
