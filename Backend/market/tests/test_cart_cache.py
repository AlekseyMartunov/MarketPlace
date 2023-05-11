import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from http.cookies import SimpleCookie
from objects.models import User
from django.core.cache import cache


@pytest.fixture
def set_up():
    url = "http://localhost:8000/api/v1/cart/"
    user_1 = User.objects.create_user(
        username="Dima",
        password="h743kJdLLd3hs&9k6dkG",
        email='someTestemail@mail.com'
    )

    client_authenticated = APIClient()
    token = RefreshToken.for_user(user_1)
    client_authenticated.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')

    client_no_authenticated = APIClient()

    cache.clear()

    return client_authenticated, client_no_authenticated, url, user_1


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_set_authenticated(set_up):
    client_authenticated, client_no_authenticated, url, _ = set_up
    data = {
        "some_name": "some_test",
        "some_age": 15
    }

    response = client_authenticated.post(url, data)

    assert response.status_code == 201
    assert cache.get('user:1:cart') == data
    assert response.data == data

    cache.clear()


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_set_no_authenticated(set_up):
    client_authenticated, client_no_authenticated, url, _ = set_up

    data = {
        "some_name": "some_test",
        "some_age": 29
    }

    response = client_no_authenticated.post(url, data)

    card_id = response.client.cookies['cart_id'].value
    key = f'user:{card_id}:cart'

    assert response.status_code == 201
    assert cache.get(key) == data
    assert response.data == data

    cache.clear()


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_set_and_get_authenticated(set_up):
    client_authenticated, client_no_authenticated, url, user_1 = set_up

    data = {
        "some_name": "some_test",
        "some_age": 29,
        "x": 'red'
    }

    response = client_authenticated.post(url, data)

    assert response.status_code == 201
    assert response.data == data
    assert cache.get('user:1:cart') == data

    response = client_authenticated.get(url)

    assert response.status_code == 200
    assert response.data == data
    assert cache.get('user:1:cart') == data

    cache.clear()


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_set_and_get_no_authenticated(set_up):
    client_authenticated, client_no_authenticated, url, user_1 = set_up

    data = {
        "some_name": "some_test",
        "some_age": 29,
        "new": True,
    }

    response = client_no_authenticated.post(url, data)

    card_id = response.client.cookies['cart_id'].value
    key = f'user:{card_id}:cart'

    assert response.status_code == 201
    assert response.data == data
    assert cache.get(key) == data

    response = client_no_authenticated.get(url)

    assert response.status_code == 200
    assert response.data == data
    assert cache.get(key) == data

    cache.clear()


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_registration_after_creating_cart(set_up):
    client_authenticated, client_no_authenticated, url, user_1 = set_up

    data = {
        "some_name": "some_test",
        "some_age": 259
    }

    response = client_no_authenticated.post(url, data)

    assert 'cart_id' in response.client.cookies

    card_id = response.client.cookies['cart_id'].value
    key = f'user:{card_id}:cart'

    assert response.status_code == 201
    assert response.data == data
    assert cache.get(key) == data

    client_authenticated.cookies = SimpleCookie({'cart_id': card_id})
    response = client_authenticated.get(url)
    card_id = response.client.cookies['cart_id'].value

    # Почему-то COOKIE не удаляется, а просто становится пустой строкой
    assert card_id == ''
    assert cache.get(key) is None

    assert response.status_code == 200
    assert response.data == data
    assert cache.get('user:1:cart') == data

    cache.clear()


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_three_item_and_registration(set_up):
    client_authenticated, client_no_authenticated, url, user_1 = set_up

    item_1 = {
        "data": 123,
        "some_field": "some_string"
    }

    item_2 = {
        "data": 456,
        "some_field": "some_new_string_string"
    }

    item_3 = {
        "text": 789,
        "another_text": 100
    }

    client_no_authenticated.post(url, item_1)
    client_no_authenticated.post(url, item_2)
    client_no_authenticated.post(url, item_3)

    response = client_no_authenticated.get(url)

    assert response.status_code == 200
    assert response.data == [item_1, item_2, item_3]

    card_id = response.client.cookies['cart_id'].value

    assert card_id is not None

    client_authenticated.cookies = SimpleCookie({'cart_id': card_id})

    response = client_authenticated.get(url)

    assert response.status_code == 200
    assert response.data == [item_1, item_2, item_3]

    cache.clear()






























