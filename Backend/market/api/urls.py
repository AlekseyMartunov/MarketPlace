from django.urls import path
from api.views import ItemList


urlpatterns = [
    path('ItemList', ItemList.as_view()),
]