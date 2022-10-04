from django.apps import AppConfig


class TransitApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transit_api'

    def ready(self):
        from . import updater
        updater.start()
