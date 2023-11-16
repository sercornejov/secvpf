from django.apps import AppConfig


class PfappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pfapp'
    verbouse_name='perfiles'
    
    def ready(self):
        import pfapp.signals
