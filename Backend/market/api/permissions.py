from rest_framework.permissions import BasePermission


class ShopOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        owner = obj.shop.owner
        return user == owner

