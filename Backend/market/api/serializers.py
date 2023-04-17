from rest_framework import serializers
from objects.models import Item, Category, Shop


class ItemListSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Item
        fields = ('name', 'slug', 'shop', 'amount', 'pk', 'images', 'price')


class ItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('name', 'description', 'amount', 'price', 'category', 'shop', 'slug', 'created_time')
        read_only_fields = ('slug', 'created_time')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'slug', 'parent')


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('pk', 'name', 'slug')





