from _pytest import mark
from django.contrib.auth import get_user_model
from django.test import TestCase


def test_login(client):
    response = client.post('/login/', {'username': 'user123', 'password': 'password123'})

    assert response.status_code == 200


def test_create_user(client):
    # Send a POST request to the create user endpoint
    response = client.post('/create-user/', {'username': 'user123', 'password': 'password123'})

    # Assert that the request was successful and that a new user was created
    assert response.status_code == 201
    assert get_user_model().objects.count() == 1
