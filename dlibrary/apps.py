from django.apps import AppConfig


class DlibraryConfig(AppConfig):
    name = 'dlibrary'
    def ready(self):
        import dlibrary.mysignals
