from rest_framework import serializers
from objects.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'price', 'amount', 'slug')



