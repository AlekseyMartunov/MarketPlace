from rest_framework import serializers
from objects.models import Item, Category
from api.services import OnlyAllowedParams


class ItemListSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Item
        fields = ('name', 'slug', 'shop', 'amount', 'pk', 'images', 'price', 'params')


class ItemDetailSerializer(serializers.ModelSerializer):
    @OnlyAllowedParams()
    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Item
        fields = ('name', 'description', 'amount', 'price', 'category', 'params', 'shop', 'slug', 'created_time')
        read_only_fields = ('slug', 'created_time')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'slug', 'parent')





