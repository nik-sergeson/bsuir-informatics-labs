from django.apps import AppConfig
from django.conf import settings
import paypalrestsdk


class PaypalAppConfig(AppConfig):
    name = 'P2PLending.paypal'

    def ready(self):
        paypalrestsdk.configure({
            "mode": settings.PAYPAL_MODE,
            "client_id": settings.PAYPAL_ID,
            "client_secret": settings.PAYPAL_SECRET})
