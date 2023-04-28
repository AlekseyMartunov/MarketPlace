from rest_framework.response import Response
from rest_framework import generics
from django.core.cache import cache
import secrets


class CartCacheAPI(generics.ListCreateAPIView):
    """
    Класс для кеширования корзины пользователей. Если пользователь уже
    авторизован, то в базе ключ будет создаваться на основе id пользователя в базе.
    Если пользователь не авторизован, мы создаем временный токен и храним его в COOKIES.
    На основании временного токена создается ключ для кеша. Если пользователь собрал корзину
    и только потом зарегистрировался, то в кеше мы меняем ключ на новый и удаляем COOKIES.
    Дальнейшая работа с кешем будет вестись по ключу, сделанному на основе индекса бд.
    """
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = "user:" + str(request.user.pk) + ":cart"
            data = request.data
            cache.set(user, data)
            return Response(data, status=201)
        else:
            token = secrets.token_hex(16)
            user = "user:" + token + ":cart"
            data = request.data
            cache.set(user, data)
            res = Response(data, status=201)
            res.set_cookie('cart_id', token)
            return res

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            token = request.COOKIES.get('cart_id')
            if token is None:
                user = "user:" + str(request.user.pk) + ":cart"
                data = cache.get(user)
                return Response(data)
            else:
                # Если пользователь авторизован и у него есть токен корзины,
                # то в кеше мы меняем ему ключ, основанный на токене, на ключ который
                # основан на его pk.
                user = "user:" + token + ":cart"
                data = cache.get(user)
                cache.delete(user)
                new_user = "user:" + str(request.user.pk) + ":cart"
                cache.set(new_user, data)
                res = Response(data)
                res.delete_cookie('cart_id')
                return res

        else:
            token = request.COOKIES.get('cart_id')
            if token is None:
                return Response()
            user = "user:" + token + ":cart"
            data = cache.get(user)
            return Response(data)

