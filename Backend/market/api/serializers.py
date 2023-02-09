from rest_framework import serializers

from objects.models import Item
from api.services import OnlyAllowedParams


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'slug')


class ItemDetailSerializer(serializers.ModelSerializer):

    @OnlyAllowedParams('params', 1)
    def create(self, validated_data):
        return super().create(validated_data)

    @OnlyAllowedParams('params', 2)
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = Item
        fields = ('name', 'description', 'amount', 'category', 'slug', 'params')




