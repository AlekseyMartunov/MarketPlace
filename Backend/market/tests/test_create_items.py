import pytest

# export DJANGO_SETTINGS_MODULE=market.settings

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from objects.models import Category, User, Shop, Item

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
            "mass": {
                "type": "number",
                "min": 0,
                "max": 10000
            },
            "color": {
                    "type": "choice",
                    "choice": ["red", "blue", "green", "black"],
                    "many": False
            }

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
        "amount": 10,
        "price": 500,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": 500,
            "color": ["blue", ]
        }
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    time = Item.objects.get(name="test").created_time

    true_data = {
        "name": "test",
        "description": "2",
        "amount": 10,
        "price": "500.00",
        "category": 1,
        "shop": 1,
        "slug": "test",
        "params": {
            "mass": 500,
            "color": ["blue", ]
        },
        "created_time": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_missing_key(set_up):
    client, shop, category = set_up
    data = {
        "name": "testName",
        "description": "2",
        "amount": 400,
        "price": "500.00",
        "category": 1,
        "shop": 1,
        "params": {

        }
    }

    true_data = {
        "mass": "missing key",
        "color": "missing key",
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_wrong_type_fields(set_up):
    client, shop, category = set_up
    data = {
        "name": "test",
        "description": "2",
        "amount": 10,
        "price": 500,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": "some text",
            "color": ["blue", ]
        }
    }
    true_data = {
        "mass": "wrong type"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_wrong_type_and_missing_key(set_up):
    client, shop, category = set_up
    data = {
        "name": "test",
        "description": "2",
        "amount": 10,
        "price": 500,
        "category": 1,
        "shop": 1,
        "params": {
            "MASS" : "this name is wrong because it is in uppercase",
            "color": ["some another color", ]
        }
    }
    true_data = {
        "mass": "missing key",
        "color": "wrong type"
    }

    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_wrong_number_type(set_up):
    client, shop, category = set_up
    data = {
        "name": "test",
        "description": "2",
        "amount": 10,
        "price": 500,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": -100,
            "color": ["some another color", ]
        }
    }
    true_data = {
        "mass": "wrong type",
        "color": "wrong type"
    }

    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data == true_data

    data = {
        "name": "test",
        "description": "2",
        "amount": 10,
        "price": 500,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": 30_000,
            "color": ["green", ]
        }
    }
    true_data = {
        "mass": "wrong type",
    }

    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_two_calls(set_up):
    client, shop, category = set_up
    # data for first call
    data_1 = {
        "name": "test",
        "description": "2",
        "amount": 10,
        "price": 500,
        "category": 1,
        "shop": 1,
        "params": {
            "color": ["blue", "red", "green"]
        }
    }
    true_data_1 = {
        "mass": "missing key",
        "color": "wrong type"
    }
    # data for second call
    data_2 = {
        "name": "test",
        "description": "2",
        "amount": 10,
        "price": 500,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": 500,
            "color": ["blue", "red", "green"]
        }
    }
    true_data_2 = {
        "color": "wrong type"
    }

    # first call
    response = client.post(url, data_1, format='json')
    assert response.status_code == 400
    assert response.data == true_data_1

    # second call
    response = client.post(url, data_2, format='json')
    assert response.status_code == 400
    assert response.data == true_data_2




@pytest.fixture
def set_up_many_params():
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
            "mass": {
                    "type": "number",
                    "min": 100,
                    "max": 500,
            },
            "price": {
                    "type": "number",
                    "min": 0,
                    "max": 100000,
            },
            "color": {
                    "type": "choice",
                    "choice": ["red", "blue", "green", "black"],
                    "many": True
            },
            "status": {
                "type": "choice",
                "choice": ["vip", "all", "private"],
                "many": False
            }

        }
    )

    client = APIClient()
    token = RefreshToken.for_user(user_1)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')

    return client, shop_1, cat_1


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_many_params(set_up_many_params):
    client, shop, category = set_up_many_params
    data = {
        "name": "test",
        "description": "2",
        "amount": 10,
        "price": 500,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": 500,
            "price": 300,
            "color": ["blue", "green"],
            "status": ["vip", ]
        }
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    time = Item.objects.get(name="test").created_time

    true_data = {
        "name": "test",
        "description": "2",
        "amount": 10,
        "price": "500.00",
        "category": 1,
        "shop": 1,
        "slug": "test",
        "params": {
            "mass": 500,
            "price": 300,
            "color": ["blue", "green"],
            "status": ["vip", ]
        },
        "created_time": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_wrong_fields_type_many_params(set_up_many_params):
    client, shop, category = set_up_many_params
    data = {
        "name": "test",
        "description": "2",
        "amount": 10,
        "price": 500,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": ["1", ],
            "price": True,
            "color": ["blue", "GREEN"],
            "status": ["vip", "all"]
        }
    }

    true_data = {
        "mass": "wrong type",
        "price": "wrong type",
        "color": "wrong type",
        "status": "wrong type",
    }

    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data == true_data














