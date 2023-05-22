from rest_framework import viewsets
from rest_framework import generics
from django_filters import rest_framework as filters
from django.db.models import Avg

from rest_framework.permissions import IsAdminUser, AllowAny
from api.permissions import ShopOwner
from api.service import MyOrderingFilter
from api.service import ItemFilter
from objects.models import Item, Category, Shop
from api.serializers import ItemListSerializer, ItemDetailSerializer, CategoryDetailSerializer,\
                            ShopListSerializer


class ItemAPI(viewsets.ModelViewSet):
    """
    Класс для работы с товарами
    """
    queryset = Item.objects.all()
    lookup_field = 'slug'
    serializer_class = ItemDetailSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Item.objects.filter(slug=slug).annotate(rating=Avg("RatingReviewsBookmark__rating"))

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'create'):
            permission_classes = [IsAdminUser | ShopOwner]
        else:
            permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]


class CategoriesAPI(viewsets.ModelViewSet):
    """
    Класс для работы с категориями
    """
    queryset = Category.objects.all()
    lookup_field = 'slug'
    serializer_class = CategoryDetailSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'create'):
            permission_classes = [IsAdminUser, ]
        else:
            permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]


class FilterListItems(generics.ListAPIView):
    """
    Класс, для реализации фильтрации и сортировки в запросе
    ожидает на вход:
    api/v1/search-items/category_slug?query_params"
    """

    def get_queryset(self):
        category = self.kwargs['category_slug']
        return Item.objects.filter(category__slug=category).annotate(rating=Avg("RatingReviewsBookmark__rating"))

    serializer_class = ItemListSerializer
    filter_backends = (filters.DjangoFilterBackend, MyOrderingFilter)
    filterset_class = ItemFilter
    ordering_fields = ("price", )


class ShopApi(generics.ListAPIView):
    """
    Класс для получения параметров во время фильтрации товаров.
    Пользователь выбирает категорию товара, и в окне фильтрации появляются
    магазины с такой категорий
    """
    queryset = Category.objects.all()
    lookup_field = 'categories__name'
    serializer_class = ShopListSerializer

    def get_queryset(self):
        category = self.kwargs['category_slug']
        return Shop.objects.filter(categories__slug=category)











