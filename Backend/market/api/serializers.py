from rest_framework import serializers

from objects.models import Item
from api.services import OnlyAllowedParamsCreate, OnlyAllowedParamsUpdate


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'slug')


class ItemDetailSerializer(serializers.ModelSerializer):

    @OnlyAllowedParamsCreate(validate_field='params')
    def create(self, validated_data):
        return super().create(validated_data)

    @OnlyAllowedParamsUpdate(validate_field='params')
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = Item
        fields = ('name', 'description', 'amount', 'category', 'params', 'slug')
        read_only_fields = ('slug', )





