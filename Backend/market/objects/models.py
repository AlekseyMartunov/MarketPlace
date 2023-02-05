from django.db import models
from objects.utils import unique_slugify


class Item(models.Model):
    """Класс для описания товара"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    amount = models.PositiveIntegerField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    params = models.JSONField()

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Photos(models.Model):
    """Класс для хранения изображений"""
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to="photos/%Y/%m/%d/")


class Category(models.Model):
    """Класс для описания категорий"""
    name = models.CharField(max_length=100)
    allowed_params = models.JSONField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

