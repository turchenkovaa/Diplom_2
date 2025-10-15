import pytest
import allure
from api_client.api_client import StellarBurgersAPI
from help.data import ORDER_TEST_DATA


class TestCreateOrder:
    @allure.title("Создать заказ с авторизацией")
    def test_create_order_with_auth(self, authenticated_user):
        api_client = authenticated_user
        
        with allure.step("Создаем заказ с авторизацией"):
            ingredients = ORDER_TEST_DATA["valid_ingredients"]
            response = api_client.create_order(ingredients, auth=True)
        
        with allure.step("Проверяем успешное создание"):
            assert response.status_code == 200, f"Код должен быть 200, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] == True, "Должен быть success: true"
            assert "name" in response_data, "Должно вернуться название заказа"
            assert "order" in response_data, "Должен вернуться объект заказа"
            assert "number" in response_data["order"], "Должен вернуться номер заказа"

    @allure.title("Создать заказ без авторизации")
    def test_create_order_without_auth(self):
        api_client = StellarBurgersAPI()
        with allure.step("Создаем заказ без авторизации"):
            ingredients = ORDER_TEST_DATA["valid_ingredients"]
            response = api_client.create_order(ingredients, auth=False)
            
        with allure.step("Проверяем ошибку авторизации"):
            assert response.status_code == 401, f"Должна быть ошибка 401, получена {response.status_code}"


    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        api_client = StellarBurgersAPI()
        with allure.step("Создаем заказ без ингредиентов"):
            ingredients = ORDER_TEST_DATA["empty_ingredients"]
            response = api_client.create_order(ingredients, auth=True)
        with allure.step("Проверяем ошибку валидации"):
            assert response.status_code == 400, f"Должна быть 400, получена {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is False
            assert "must be provided" in response_data.get("message", "")


    @allure.title("Создание заказа с неправильными ингредиентами")
    def test_create_order_invalid_ingredients(self):
        api_client = StellarBurgersAPI()
        with allure.step("Создаем заказ с неправильными ингредиентами"):
            ingredients = ORDER_TEST_DATA["invalid_ingredients"]
            response = api_client.create_order(ingredients, auth=True)
        with allure.step("Проверяем ошибку сервера"):
            assert response.status_code == 500, f"Должна быть ошибка 500, получена {response.status_code}"