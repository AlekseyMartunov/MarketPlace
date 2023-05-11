from django.urls import path
from cache.views import CartCacheAPI

urlpatterns = [
    path('cart/', CartCacheAPI.as_view()),
]