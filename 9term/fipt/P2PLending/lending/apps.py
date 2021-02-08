from django.apps import AppConfig


class LendingAppConfig(AppConfig):
    name = 'P2PLending.lending'

    def ready(self):
        import P2PLending.lending.signal_receivers
        from P2PLending.lending.raiting import fit_model
        fit_model()
