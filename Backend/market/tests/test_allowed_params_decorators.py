import pytest
from rest_framework.test import APIClient

from objects.models import Item, Category


url = "http://127.0.0.1:8000/api/v1/items"
client = APIClient()


@pytest.mark.django_db(transaction=True, reset_sequences=True)
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


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_missing_key():
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
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_wrong_type_fields():
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
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_wrong_type_and_missing_key():
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
    assert response.data == true_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_two_calls():
    cat_1 = Category.objects.create(
        name='test_cat_1',
        allowed_params={
            "mass": "number",
            "color": "bool",
            "price": "number",
            "text": "string"
        }
    )
    # data for first call
    data_1 = {
        "name": "testName",
        "description": "2",
        "amount": 30704,
        "category": 1,
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

    # data for first call
    response = client.post(url, data_1, format='json')
    assert response.data == true_data_1

    # data for second call
    response = client.post(url, data_2, format='json')
    assert response.data == true_data_2







