import pytest
from rest_framework.test import APIClient
from objects.models import Category, User, Shop, Item


@pytest.fixture
def set_up():
    url = "http://127.0.0.1:8000/api/v1/search-items"
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

    cars_shop_2 = Shop.objects.create(
        name="cars_shop_2",
        description="cars_shop_2",
        owner=user,
    )
    cars_shop_2.categories.add(cars)

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

    lancer = Item.objects.create(
        name="lancer",
        description="lancer",
        price=300_000,
        amount=2,
        category=cars,
        shop=cars_shop_2
    )

    fish = Item.objects.create(
        name="fish",
        description="fish",
        price=800,
        amount=10,
        category=food,
        shop=food_shop
    )

    apple = Item.objects.create(
        name="apple",
        description="apple",
        price=100,
        amount=500,
        category=food,
        shop=food_shop
    )

    milk = Item.objects.create(
        name="milk",
        description="milk",
        price=150,
        amount=100,
        category=food,
        shop=food_shop
    )

    return url


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_filter_category(set_up):
    url = set_up
    url += "/cars"
    true_data = [
        {
            "name": "lada",
            "slug": "lada",
            "amount": 1,
            "shop_name": "cars_shop",
            "pk": 1,
            "images": [],
            "price": "100000.00"
        },
        {
            "name": "lancer",
            "slug": "lancer",
            "amount": 2,
            "shop_name": "cars_shop_2",
            "pk": 2,
            "images": [],
            "price": "300000.00"
        },
    ]

    client = APIClient()
    response = client.get(url, format='json')

    assert response.status_code == 200
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_filter_shop(set_up):
    url = set_up
    url += "/cars?shop=cars_shop_2"

    true_data = [
        {
            "name": "lancer",
            "slug": "lancer",
            "amount": 2,
            "shop_name": "cars_shop_2",
            "pk": 2,
            "images": [],
            "price": "300000.00"
        },
    ]

    client = APIClient()
    response = client.get(url, format='json')

    assert response.status_code == 200
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_filter_shop_and_max_price(set_up):
    url = set_up
    url += "/cars?shop=cars_shop&max_price=150000"

    true_data = [
        {
            "name": "lada",
            "slug": "lada",
            "amount": 1,
            "shop_name": "cars_shop",
            "pk": 1,
            "images": [],
            "price": "100000.00"
        },
    ]

    client = APIClient()
    response = client.get(url, format='json')

    assert response.status_code == 200
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_filter_empty(set_up):
    url = set_up
    url += "/food?shop=cars_shop"

    true_data = []

    client = APIClient()
    response = client.get(url, format='json')

    assert response.status_code == 200
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_filter_order(set_up):
    url = set_up
    url += "/food?order=price"

    true_data = [
        {
            "name": "apple",
            "slug": "apple",
            "amount": 500,
            "shop_name": "food_shop",
            "pk": 4,
            "images": [],
            "price": "100.00"
        },
        {
            "name": "milk",
            "slug": "milk",
            "amount": 100,
            "shop_name": "food_shop",
            "pk": 5,
            "images": [],
            "price": "150.00"
        },
        {
            "name": "fish",
            "slug": "fish",
            "amount": 10,
            "shop_name": "food_shop",
            "pk": 3,
            "images": [],
            "price": "800.00"
        },
    ]

    client = APIClient()
    response = client.get(url, format='json')

    assert response.status_code == 200
    assert response.data == true_data


