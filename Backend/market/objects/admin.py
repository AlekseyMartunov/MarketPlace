from django.contrib import admin
from objects.models import Item, Photos, Category, Shop,\
    RatingReviewsBookmark, OrderItem, Order


class AdminPhotos(admin.StackedInline):
    model = Photos


@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    readonly_fields = ('slug', )
    inlines = [AdminPhotos]


class AdminSubCategory(admin.StackedInline):
    model = Category
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [AdminSubCategory]


@admin.register(Shop)
class AdminShop(admin.ModelAdmin):
    list_display = ('name', 'owner')
    prepopulated_fields = {'slug': ('name', 'owner')}


@admin.register(RatingReviewsBookmark)
class AdminRatingReviewsBookmark(admin.ModelAdmin):
    list_display = ('user', 'item', 'review', 'rating', 'in_bookmark')


@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('pk', 'item', 'order', 'price', 'amount')


@admin.register(Order)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('pk', 'user', 'data', 'price', 'status')


