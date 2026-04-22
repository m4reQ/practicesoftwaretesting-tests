import pytest
import string
import random
import requests
from typing import Generator, Any
from selenium.webdriver import Firefox

@pytest.fixture(scope='function')
def driver() -> Generator[Firefox, Any, None]:
    _driver = Firefox()
    yield _driver

    _driver.quit()

@pytest.fixture(scope='function')
def random_email() -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(8)) + '@gmail.com'

@pytest.fixture(scope='function')
def shopping_cart() -> str:
    response = requests.post('https://api.practicesoftwaretesting.com/carts')
    assert response.status_code == 201

    return response.json()['id']

@pytest.fixture(scope='function')
def random_user(random_email: str) -> str:
    user_password = 'TestPassword123.'
    user_create_response = requests.get(
        'https://api.practicesoftwaretesting.com/users/register',
        json={
            'first_name': 'Foo',
            'last_name': 'Bar',
            'address': {
                'street': 'Street 1',
                'city': 'City',
                'state': 'State',
                'country': 'Country',
                'postal_code': '1234AA'
            },
            'phone': '0987654321',
            'dob': '1970-01-01',
            'password': user_password,
            'email': random_email})
    assert user_create_response.status_code == 201

    user_login_response = requests.get(
        'https://api.practicesoftwaretesting.com/users/login',
        json={
            'email': random_email,
            'password': user_password})
    assert user_login_response.status_code == 200

    return user_login_response.json()['access_token']

@pytest.fixture(scope='function')
def admin_user() -> str:
    user_login_response = requests.post(
        'https://api.practicesoftwaretesting.com/users/login',
        json={
            'email': 'admin@practicesoftwaretesting.com',
            'password': 'welcome01'})
    assert user_login_response.status_code == 200

    return user_login_response.json()['access_token']