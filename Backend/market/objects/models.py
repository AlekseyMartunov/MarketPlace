import os

from django.core.validators import MinValueValidator
from django.db import models
from objects.utils import unique_slugify
from django.contrib.auth.models import User

from market.settings import HOST


class Item(models.Model):
    """Класс для описания товара"""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        validators=[MinValueValidator(limit_value=0.01), ]
    )
    created_time = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    params = models.JSONField()

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Photos(models.Model):
    """Класс для хранения изображений"""
    item = models.ForeignKey(Item, related_name="images", on_delete=models.CASCADE)
    photos = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return f"{HOST}/media/{self.photos.name}"

    def delete(self):
        """Автоматическое удаление изображений при удалении объекта модели Item"""
        if os.path.exists(self.photos.path):
            os.remove(self.photos.path)
        return super().delete()


class Category(models.Model):
    """Класс для описания категорий"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    allowed_params = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.name






