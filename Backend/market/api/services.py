from django_filters import rest_framework as filters
from objects.models import Item


class ItemFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    price = filters.NumberFilter()

    class Meta:
        model = Item
        fields = ['category', 'price']

