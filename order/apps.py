from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'

    def ready(self) -> None:
        super().ready()

        # to register your custom if you use custom structure folder
        from order import signals
