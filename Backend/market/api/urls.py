from django.urls import path
from api.views import ItemListAPI


urlpatterns = [
    path('items', ItemListAPI.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('items/<int:pk>', ItemListAPI.as_view({
        'get': 'retrieve',
    })),
]