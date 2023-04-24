from django.utils.translation import gettext_lazy as _
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from objects.models import Item


class ItemFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    shop = filters.CharFilter(field_name="shop__slug", lookup_expr="exact")

    class Meta:
        model = Item
        fields = ['price', 'category']


class MyOrderingFilter(OrderingFilter):
    ordering_param = _('order')
