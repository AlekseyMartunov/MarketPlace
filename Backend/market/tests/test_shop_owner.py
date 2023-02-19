import pytest

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from objects.models import Category, User, Shop, Item


url = "http://127.0.0.1:8000/api/v1/items/test_name"


@pytest.fixture
def set_up():
    user_owner = User.objects.create_user(
        username='JohnOwner',
        password='jlen63becccatlccesu4o',
    )
    user = User.objects.create_user(
        username='John',
        password='jlen6xx3beatlesu4o',
    )
    Shop.objects.create(
        name="test_name_1",
        description="test_description_1",
        owner=user_owner
    )
    Category.objects.create(
        name='test_cat_1',
        allowed_params={
            "mass": "number"
        }
    )
    Item.objects.create(
        name="test_name",
        description="test",
        amount=300,
        category_id=1,
        shop_id=1,
        params={
        "mass": 500
        }
    )
    return user, user_owner


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_update_ower(set_up):
    user, user_owner = set_up

    client = APIClient()
    token = RefreshToken.for_user(user_owner)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')

    data = {
        "name": "test_name",
        "description": "test",
        "amount": 400,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": 500,
        }
    }
    true_data = {
        "name": "test_name",
        "description": "test",
        "amount": 400,
        "category": 1,
        "shop": 1,
        "slug": "test_name",
        "params": {
            "mass": 500,
        }
    }

    response = client.put(url, data, format='json')
    assert response.status_code == 200
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_update_another_user(set_up):
    user, user_owner = set_up

    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')

    data = {
        "name": "test_name",
        "description": "test",
        "amount": 400,
        "category": 1,
        "shop": 1,
        "params": {
            "mass": 500,
        }
    }
    true_data = {
        "detail": "You do not have permission to perform this action."
    }

    response = client.put(url, data, format='json')
    assert response.status_code == 403
    assert response.data == true_data





