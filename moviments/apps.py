from django.apps import AppConfig


class MovimentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moviments'


class MovimentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moviments'

    def ready(self):
        import moviments.signals