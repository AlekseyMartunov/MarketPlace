import pytest

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from objects.models import Category, User, Shop


url = "http://127.0.0.1:8000/api/v1/items"


@pytest.fixture
def set_up():
    user_1 = User.objects.create_user(
        username='John',
        password='jlen63beatlesu4o',
        email='testmail@list.com'
    )
    shop_1 = Shop.objects.create(
        name="test_name_1",
        description="test_description_1",
        owner=user_1
    )
    cat_1 = Category.objects.create(
        name='test_cat_1',
        allowed_params={
            "mass": "number",
            "color": "bool",
            "price": "number",
            "text": "string"
        }
    )

    client = APIClient()
    token = RefreshToken.for_user(user_1)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')

    return client, shop_1, cat_1


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create(set_up):
    client, shop, category = set_up
    data = {
        "name": "test",
        "description": "2",
        "amount": 30704,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": 500,
            "color": True,
            "price": 500,
            "text": "some text",
            "new": 123
        }
    }
    true_data = {
        "name": "test",
        "description": "2",
        "amount": 30704,
        "category": 1,
        "shop": 1,
        "slug": "test",
        "params": {
            "mass": 500,
            "color": True,
            "price": 500,
            "text": "some text"

        }
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_missing_key(set_up):
    client, shop, category = set_up
    data = {
        "name": "testName",
        "description": "2",
        "amount": 30704,
        "category": 1,
        "shop": 1,
        "params": {
            "color": True,
            "text": "some text",
            "new": 123
        }
    }
    true_data = {
        "mass": [
            "missing key"
        ],
        "price": [
            "missing key"
        ]
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_wrong_type_fields(set_up):
    client, shop, category = set_up
    data = {
        "name": "testName",
        "description": "2",
        "amount": 30704,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": 7584,
            "color": "some_string",
            "price": True,
            "text": 7594
        }
    }
    true_data = {
        "color": [
            "This field should be bool"
        ],
        "price": [
            "This field should be number"
        ],
        "text": [
            "This field should be string"
        ]
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_wrong_type_and_missing_key(set_up):
    client, shop, category = set_up
    data = {
        "name": "testName",
        "description": "2",
        "amount": 30704,
        "category": 1,
        "shop": 1,
        "params": {
            "color": "some_string",
            "price": 7584,
            "text": 7594
        }
    }
    true_data = {
        "mass": [
            "missing key"
        ],
        "color": [
            "This field should be bool"
        ],
        "text": [
            "This field should be string"
        ]
    }

    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_two_calls(set_up):
    client, shop, category = set_up
    # data for first call
    data_1 = {
        "name": "testName",
        "description": "2",
        "amount": 30704,
        "category": 1,
        "shop": 1,
        "params": {
            "color": "some_string",
            "price": True,
            "text": "some text"
        }
    }
    true_data_1 = {
        "mass": [
            "missing key"
        ],
        "color": [
            "This field should be bool"
        ],
        "price": [
            "This field should be number"
        ]
    }
    # data for second call
    data_2 = {
        "name": "testName",
        "description": "2",
        "amount": 30704,
        "category": 1,
        "shop": 1,
        "params": {
            "color": False,
            "price": True,
            "text": "some text"
        }
    }
    true_data_2 = {
        "mass": [
            "missing key"
        ],
        "price": [
            "This field should be number"
        ]
    }

    # first call
    response = client.post(url, data_1, format='json')
    assert response.status_code == 400
    assert response.data == true_data_1

    # second call
    response = client.post(url, data_2, format='json')
    assert response.status_code == 400
    assert response.data == true_data_2




