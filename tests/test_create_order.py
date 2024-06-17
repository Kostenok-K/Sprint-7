import allure
import requests
import pytest
from data import URL


@allure.suite('Проверка на создание заказа')
class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа')
    @allure.description('Cоздания заказа с разными цветами, их комбинацией и отсутствием цвета, Код - 201')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        response = requests.post(URL.ORDER, json=payload)
        assert response.status_code == 201 and 'track' in response.text
