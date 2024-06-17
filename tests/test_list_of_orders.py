import allure
import requests
from data import URL


@allure.suite('Список заказов')
class TestListOfOrders:
    @allure.title('Проверка списка заказов')
    @allure.description('Проверяем возврата списка заказов, Код - 200')
    def test_oder_list(self):
        response = requests.get(URL.ORDER)
        assert response.status_code == 200 and type(response.json()['orders']) is list
