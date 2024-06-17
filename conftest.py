import helpers
import requests
import pytest
from data import URL



@pytest.fixture
def unregistered_courier():
    login, password, first_name = helpers.generate_unregistered_courier()
    payload = {
        'login': login,
        'password': password,
        'firstName': first_name
    }

    yield payload
    del payload['firstName']
    response = requests.post(URL.LOGIN, data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'{URL.COURIER}{courier_id}')


@pytest.fixture
def registered_courier():
    login, password, first_name = helpers.register_new_courier_and_return_login_password()
    payload = {
        'login': login,
        'password': password
    }

    yield payload
    response = requests.post(URL.LOGIN, data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'{URL.COURIER}{courier_id}')
