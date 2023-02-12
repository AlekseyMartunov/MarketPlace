import pytest
from rest_framework.test import APIClient

from objects.models import Item, Category


url = "http://127.0.0.1:8000/api/v1/items"
client = APIClient()


@pytest.mark.django_db
def test_create():
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
            "text": "some text",
            "new": 123
        }
    }
    true_data = {
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

    response = client.post(url, data, format='json')
    assert response.data == true_data