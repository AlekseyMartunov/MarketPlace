from django.urls import path
from api.views import ItemListAPI


urlpatterns = [
    path('items', ItemListAPI.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('items/<slug:slug>', ItemListAPI.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]