import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient, APIRequestFactory
from objects.models import Category, User, Shop, Item


@pytest.fixture
def set_up():
    user = User.objects.create_user(
        username="Dima",
        password="h743kJdLLd3hs&9k6dkG",
        email='someTestemail@mail.com'
    )

    cars = Category.objects.create(
        name="cars",
        parent=None
    )

    food = Category.objects.create(
        name="food",
        parent=None
    )

    cars_shop = Shop.objects.create(
        name="cars_shop",
        description="cars_shop",
        owner=user,
    )
    cars_shop.categories.add(cars)

    food_shop = Shop.objects.create(
        name="food_shop",
        description="food_shop",
        owner=user,
    )
    food_shop.categories.add(food)

    lada = Item.objects.create(
        name="lada",
        description="lada",
        price=100_000,
        amount=1,
        category=cars,
        shop=cars_shop
    )

    fish = Item.objects.create(
        name="lada",
        description="lada",
        price=1_000,
        amount=100,
        category=food,
        shop=food_shop
    )

    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')

    return client, lada, fish


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_filter_category(set_up):
    client, lada, fish = set_up
    url = "http://127.0.0.1:8000/api/v1/search-items"  #shop=cars_shop"

    # factory = APIRequestFactory()
    # request = factory.get(url)
    response = client.get(url, format='json')

    assert response.status_code == 200
    assert response.data == 20
