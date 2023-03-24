from django.apps import AppConfig


class ObjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'objects'

    def ready(self):
        from objects.signals import auto_delete_images_on_delete_model_object
