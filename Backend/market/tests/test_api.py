from rest_framework import status
from rest_framework.test import APITestCase


class ItemApiTest(APITestCase):
    def test_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/ItemList')
        self.assertEqual(status.HTTP_200_OK, response.status_code)



