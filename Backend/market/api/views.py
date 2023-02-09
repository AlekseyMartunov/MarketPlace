from rest_framework import viewsets
from rest_framework.response import Response

from objects.models import Item
from api.serializers import ItemListSerializer, ItemDetailSerializer


class ItemListAPI(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    lookup_field = 'slug'
    serializer_class = ItemDetailSerializer

    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemListSerializer(queryset, many=True)
        return Response(serializer.data)




