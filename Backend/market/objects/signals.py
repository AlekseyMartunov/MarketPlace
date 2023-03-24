from django.db.models.signals import pre_delete
from django.dispatch import receiver
from objects.models import Item


@receiver(pre_delete, sender=Item)
def auto_delete_images_on_delete_model_object(sender, instance, **kwargs):
    """Автоматическое удаление изображений при удалении объекта модели Item"""
    images = instance.images.all()
    [obj.delete() for obj in images]



