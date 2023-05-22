from rest_framework.response import Response
from rest_framework import generics
from django.core.cache import cache
import secrets


class CacheService:
    CLEAR_COOKIES = False
    SEND_COOKIES = False
    TOKEN = ""

    def get_user_key(self):
        cookies_key = self.request.COOKIES.get('cart_id')
        if self.request.user.is_authenticated:
            if cookies_key:
                self.CLEAR_COOKIES = True
                return self.update_user_key(cookies_key)
            else:
                return "user:" + str(self.request.user.pk) + ":cart"
        else:
            if cookies_key:
                return "user:" + cookies_key + ":cart"
            else:
                token = secrets.token_hex(16)
                self.SEND_COOKIES = True
                self.TOKEN = token
                return "user:" + token + ":cart"

    def update_user_key(self, old_key):
        """
        Данный метод вызывается для создания нового ключа в кеше, который основан на user_pk.
        Когда пользователь был не авторизован мы использовали специальный токен и хранили его в
        COOKIES. Еcли пользователь авторизовался, то его данные не пропадают. Мы меняем ему ключ
        в кеше и удаляем куки ключ который использовали раньше.
        """
        new_key = "user:" + str(self.request.user.pk) + ":cart"
        old_key = "user:" + old_key + ":cart"

        data = cache.get(old_key)
        cache.delete(old_key)
        cache.set(new_key, data)
        return new_key

    def set_value(self, key, value):
        if cache.has_key(key):
            data = cache.get(key)

            if type(data) == list:
                data.append(value)
            else:
                data = [data, value]

            cache.set(key, data)
        else:
            cache.set(key, value)
        return cache.get(key)

    def get_response(self, data, status):
        res = Response(data, status=status)
        if self.SEND_COOKIES:
            res.set_cookie('cart_id', self.TOKEN)
            self.SEND_COOKIES = False

        if self.CLEAR_COOKIES:
            res.delete_cookie('cart_id')
            self.CLEAR_COOKIES = False
        return res

    def get_chache_data(self, key):
        data = cache.get(key)
        if data is None:
            data = []
        return data


class CartCacheAPI(CacheService,
                   generics.ListCreateAPIView,
                   generics.DestroyAPIView,
                   generics.UpdateAPIView,):

    def post(self, request, *args, **kwargs):
        key = self.get_user_key()
        data = self.set_value(key, request.data)
        return self.get_response(data, 201)

    def put(self, request, *args, **kwargs):
        key = self.get_user_key()
        cache.set(key, request.data)
        data = self.get_chache_data(key)
        return self.get_response(data, 200)

    def delete(self, request, *args, **kwargs):
        key = self.get_user_key()
        data = cache.get(key)
        cache.delete(key)
        return self.get_response(data, 200)

    def get(self, request, *args, **kwargs):
        key = self.get_user_key()
        data = self.get_chache_data(key)
        if type(data) != list:
            data = [data,]
        return self.get_response(data, 200)
























