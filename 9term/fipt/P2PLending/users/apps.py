from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'P2PLending.users'

    def ready(self):
        import P2PLending.users.signals
