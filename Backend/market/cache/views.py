from rest_framework import generics
from django.db import transaction
from django.db.models import F
from rest_framework.response import Response


from objects.models import OrderItem, Order, Item
from cache.service import CacheService


class CartCacheAPI(CacheService,
                   generics.ListCreateAPIView,
                   generics.DestroyAPIView,
                   generics.UpdateAPIView,):

    def post(self, request, *args, **kwargs):
        key = self.get_user_key()
        data = self.set_value_into_array(key, request.data)
        return self.get_response(data, 201)

    def put(self, request, *args, **kwargs):
        key = self.get_user_key()
        print(request.data)
        self.update_value(key, request.data)
        data = self.get_chache_data(key)
        return self.get_response(data, 200)

    def delete(self, request, *args, **kwargs):
        key = self.get_user_key()
        data = self.get_chache_data(key)
        self.remove_key(key)
        return self.get_response(data, 200)

    def get(self, request, *args, **kwargs):
        key = self.get_user_key()
        data = self.get_chache_data(key)
        if type(data) != list:
            data = [data,]
        return self.get_response(data, 200)


class CreateOrderAPI(CacheService, generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        user = request.user
        if user is None:
            return Response("You must be authenticated", status=403)
        key = self.get_user_key()
        items = self.get_chache_data(key)

        with transaction.atomic():
            total_price = 0
            print(items)
            new_order = Order.objects.create(
                user=request.user,
                price=total_price,
                status="Created",
            )

            for item in items:
                item_db = Item.objects.get(slug=item["slug"])
                item_db.amount = F("amount") - item["amount"]

                OrderItem.objects.create(
                    order=new_order,
                    item=item_db,
                    price=item["price"],
                    amount=item["amount"]
                )

        return Response({"Order_Number": new_order.pk}, status=201)






























