from django_filters import rest_framework as filters
from objects.models import Item


class ItemFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = filters.CharFilter(field_name="category__slug", lookup_expr="exact")

    class Meta:
        model = Item
        fields = ['price', 'category']