from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import ItemListAPI, CategoriesAPI


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
    path('categories', CategoriesAPI.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('categories/<slug:slug>', CategoriesAPI.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]

