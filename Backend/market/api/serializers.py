from rest_framework import serializers
from objects.models import Item, Category, Shop


class ItemListSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(
        many=True,
        read_only=True
    )
    shop_name = serializers.CharField(source='shop.name')
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        model = Item
        fields = ('name', 'slug', 'shop_name', 'amount', 'pk', 'images', 'price', 'rating')


class ItemDetailSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(source='shop.name')
    shop_slug = serializers.CharField(source='shop.slug')
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)
    images = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Item
        fields = ('name', 'description', 'amount', 'price', 'category',\
                  'shop_name', 'shop_slug', 'slug', 'created_time', 'images', 'rating')
        read_only_fields = ('slug', 'created_time', 'rating')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'slug', 'parent')


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('pk', 'name', 'slug')





