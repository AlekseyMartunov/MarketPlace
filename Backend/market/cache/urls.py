from django.urls import path
from cache.views import CartCacheAPI, CreateOrderAPI

urlpatterns = [
    path('cart/', CartCacheAPI.as_view()),
    path('create-order/', CreateOrderAPI.as_view())
]