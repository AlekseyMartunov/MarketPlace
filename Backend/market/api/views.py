from rest_framework import generics
from objects.models import Item
from api.serializers import ItemSerializer


class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
