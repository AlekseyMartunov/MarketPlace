from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from objects.models import Item
from api.serializers import ItemListSerializer, ItemDetailSerializer



class ItemListAPI(viewsets.ViewSet):
    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemDetailSerializer(item)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ItemDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



