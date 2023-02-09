from rest_framework import serializers

from objects.models import Item
from api.services import OnlyAllowedParams


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', )


class ItemDetailSerializer(serializers.ModelSerializer):
    @OnlyAllowedParams('params')
    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Item
        fields = ('name', 'description', 'amount', 'category', 'params')




