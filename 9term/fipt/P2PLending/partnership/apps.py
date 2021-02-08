from django.apps import AppConfig


class PartnershipAppConfig(AppConfig):
    name = 'P2PLending.partnership'

    def ready(self):
        import P2PLending.partnership.signals
