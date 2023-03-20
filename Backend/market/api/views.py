from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from api.permissions import ShopOwner
from objects.models import Item, Category
from api.serializers import ItemListSerializer, ItemDetailSerializer, CategoryDetailSerializer


class ItemListAPI(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    lookup_field = 'slug'
    serializer_class = ItemDetailSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'create'):
            permission_classes = [IsAdminUser | ShopOwner]
        else:
            permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemListSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoriesAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    lookup_field = 'slug'
    serializer_class = CategoryDetailSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'create'):
            permission_classes = [IsAdminUser, ]
        else:
            permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = Category.objects.filter(parent=None)
        serializer = CategoryDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug, *args, **kwargs):
        queryset = Category.objects.filter(parent__slug=slug)
        serializer = CategoryDetailSerializer(queryset, many=True)
        return Response(serializer.data)




