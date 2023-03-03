from rest_framework import serializers

from objects.models import Item, Category
from api.services import OnlyAllowedParamsCreate, OnlyAllowedParamsUpdate


class ItemListSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Item
        fields = ('name', 'slug', 'shop', 'amount', 'pk', 'images', 'price')


class ItemDetailSerializer(serializers.ModelSerializer):

    @OnlyAllowedParamsCreate(validate_field='params')
    def create(self, validated_data):
        return super().create(validated_data)

    @OnlyAllowedParamsUpdate(validate_field='params')
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = Item
        fields = ('name', 'description', 'amount', 'price', 'category', 'params', 'shop', 'slug', 'created_time')
        read_only_fields = ('slug', 'created_time')


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'slug')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'slug', 'allowed_params', 'parent')





