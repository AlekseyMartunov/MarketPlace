from rest_framework import serializers
from objects.models import Item, Category, Shop


class ItemListSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(
        many=True,
        read_only=True
    )
    shop_name = serializers.CharField(source='shop.name')

    class Meta:
        model = Item
        fields = ('name', 'slug', 'shop_name', 'amount', 'pk', 'images', 'price')


class ItemDetailSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(source='shop.name')
    shop_slug = serializers.CharField(source='shop.slug')
    images = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Item
        fields = ('name', 'description', 'amount', 'price', 'category',\
                  'shop_name', 'shop_slug', 'slug', 'created_time', 'images')
        read_only_fields = ('slug', 'created_time')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'slug', 'parent')


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('pk', 'name', 'slug')





