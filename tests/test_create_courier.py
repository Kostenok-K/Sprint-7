import allure
import helpers
import requests
import pytest
from data import URL, Answers


@allure.suite('Проверки на создание курьера')
class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера')
    @allure.description('Создаем нового курьера, Код 201 ')
    def test_create_new_courier(self, unregistered_courier):
        payload = unregistered_courier
        response = requests.post(URL.COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка создании одинаковых курьеров')
    @allure.description(f'Cоздания одинаковых курьеров, Код - 409, Ответ -  {Answers.SAME_LOGIN}')
    def test_create_same_courier(self, unregistered_courier):
        payload = unregistered_courier
        requests.post(URL.COURIER, data=payload)
        response = requests.post(URL.COURIER, data=payload)
        assert response.status_code == 409 and response.json().get('message') \
               == Answers.SAME_LOGIN

    @allure.title('Проверка обязательных полей при создании курьера')
    @allure.description(f'Удаление обязательных полей, Код - 400, Ответ - {Answers.NOT_DATA_FOR_CREATE}')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_required_fields(self, missing_field):
        login, password, first_name = helpers.generate_unregistered_courier()
        payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        del payload[missing_field]
        response = requests.post(URL.COURIER, data=payload)
        assert response.status_code == 400 and response.json().get('message') == Answers.NOT_DATA_FOR_CREATE
