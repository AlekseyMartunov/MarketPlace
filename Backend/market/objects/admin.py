from django.contrib import admin
from objects.models import Item, Photos, Category


class AdminPhotos(admin.StackedInline):
    model = Photos


@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    inlines = [AdminPhotos]


class AdminSubCategory(admin.StackedInline):
    model = Category


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'parent')
    inlines = [AdminSubCategory]

