from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, \
    TokenBlacklistView
from django.urls import path
from api.views import ItemAPI, CategoriesAPI, FilterListItems, ShopApi


urlpatterns = [
    path('items', ItemAPI.as_view({
        'post': 'create'
    })),
    path('items/<slug:slug>', ItemAPI.as_view({
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
    path('search-items/<slug:category_slug>', FilterListItems.as_view()),
    path('shops/<slug:category_slug>', ShopApi.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    
    ]

