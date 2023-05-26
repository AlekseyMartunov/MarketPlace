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
        """Функция возвращает путь по которому находится изображение"""
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

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class RatingReviewsBookmark(models.Model):
    """Класс для хранения информации о рейтинге, отзывах и закладках"""
    RARING_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (4, "5"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='RatingReviewsBookmark')
    review = models.TextField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(choices=RARING_CHOICES, blank=True, null=True)
    in_bookmark = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Отзывы рейтинг и закладки"
        verbose_name_plural = "Отзывы рейтинг и закладки"


class Order(models.Model):
    """Класс хранит информацию о заказах"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.TextField()
    price = models.DecimalField(
        max_digits=14,
        decimal_places=2)


class OrderItem(models.Model):
    """Класс хранит информацию и товарах в заказе"""
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True,)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=14,
        decimal_places=2)
    amount = models.PositiveIntegerField()







