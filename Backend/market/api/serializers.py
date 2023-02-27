from rest_framework import serializers

from objects.models import Item, Photos
from api.services import OnlyAllowedParamsCreate, OnlyAllowedParamsUpdate


class ItemListSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Item
        fields = ('name', 'slug', 'shop', 'amount', 'pk', 'images')


class ItemDetailSerializer(serializers.ModelSerializer):

    @OnlyAllowedParamsCreate(validate_field='params')
    def create(self, validated_data):
        return super().create(validated_data)

    @OnlyAllowedParamsUpdate(validate_field='params')
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = Item
        fields = ('name', 'description', 'amount', 'category', 'params', 'shop', 'slug')
        read_only_fields = ('slug', )





