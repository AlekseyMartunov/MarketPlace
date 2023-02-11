from rest_framework import status
from objects.models import Item, Category
from rest_framework.test import APITestCase


url = "http://127.0.0.1:8000/api/v1/items"


class TestAllowedParamsDecorators(APITestCase):
    def test_create(self):
        cat_1 = Category.objects.create(
            name='test_cat_1',
            allowed_params={
                "mass": "number",
                "color": "bool",
                "price": "number",
                "text": "string"
            }
        )
        data = {
            "name": "testName",
            "description": "2",
            "amount": 30704,
            "category": 1,
            "params": {
                "mass": 500,
                "color": True,
                "price": 500,
                "new": 123,
                "text": "some text"
            }
        }

        tru_data = {
            "name": "testName",
            "description": "2",
            "amount": 30704,
            "category": 1,
            "slug": "testname",
            "params": {
                "mass": 500,
                "color": True,
                "price": 500,
                "text": "some text"
            }
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.json(), tru_data)






