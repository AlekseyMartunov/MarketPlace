from django.db import models


class Item(models.Model):
    """Класс для описания товара"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.PositiveIntegerField
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

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
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

