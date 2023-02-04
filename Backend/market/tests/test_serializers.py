from objects.models import Item, Category
from collections import OrderedDict
from rest_framework.test import APITestCase


class ItemApiTest(APITestCase):
    def test_data(self):
        cat_1 = Category.objects.create(
            name='test_cat_1'
        )
        item1 = Item.objects.create(
            name='test_item_1',
            description='some_description_1',
            price=100,
            amount=10,
            category=cat_1
        )
        expected_data = OrderedDict({
            "name": "test_item_1",
            "price": '100.00',
            "amount": 10,
            "slug": item1.slug
        })
        response = self.client.get('http://127.0.0.1:8000/api/v1/ItemList')
        self.assertEqual(expected_data, *response.data)