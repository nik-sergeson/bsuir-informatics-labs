from django.dispatch import receiver
from P2PLending.users.models import UserMoney
from registration.backends.default.views import RegistrationView
from registration.signals import user_registered


@receiver(user_registered, sender=RegistrationView)
def user_registered_listener(sender, **kwargs):
    user = kwargs["user"]
    UserMoney.objects.create(user=user)
