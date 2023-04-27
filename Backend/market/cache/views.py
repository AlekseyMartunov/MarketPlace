from rest_framework.response import Response
from rest_framework import generics
from django.core.cache import cache
from django.contrib.auth.models import User


class CartCacheAPI(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
        pass

    def get(self, request, *args, **kwargs):
        cache.set('key1', 'value1')
        return Response({"1": cache.get('key1')})

