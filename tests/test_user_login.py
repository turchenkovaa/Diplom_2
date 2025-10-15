import pytest
import allure
from api_client.api_client import StellarBurgersAPI
from help.data import USER_TEST_DATA

class TestUserLogin:

    @allure.title("Успешный вход зарегистрированного пользователя")
    def test_login_user_success(self, create_and_delete_user):
        api_client, email, password, name = create_and_delete_user
        # Регистрация пользователя выполнена в фикстуре
        # Выполняем логин
        with allure.step("Вхождение для зарегистрированного пользователя"):
            response = api_client.login_user(email, password)
        
        # Проверка успешного входа
        with allure.step("Проверка корректности результата входа"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
            response_data = response.json()
            # Проверяем, что ответ содержит успех и необходимые токены
            assert response_data.get("success") is True, "Ожидалось success: true"
            assert "accessToken" in response_data, "Отсутствует accessToken в ответе"
            assert "refreshToken" in response_data, "Отсутствует refreshToken в ответе"
            # Проверяем совпадение данных пользователя
            assert response_data["user"].get("email") == email, "Email пользователя не совпадает"
            assert response_data["user"].get("name") == name, "Имя пользователя не совпадает"

    @allure.title("Попытка входа с неправильным паролем")
    def test_login_wrong_password(self, create_and_delete_user):
        api_client, email, password, _ = create_and_delete_user
        # Пользователь зарегистрирован в фикстуре
        # Пытаемся войти с неправильным паролем
        with allure.step("Вход с неверным паролем для зарегистрированного пользователя"):
            response = api_client.login_user(email, "wrong_password")
        
        # Проверка сообщения об ошибке
        with allure.step("Проверка сообщения о неправильных данных"):
            assert response.status_code == 401, f"Ожидалась ошибка 401, получен {response.status_code}"
            response_data = response.json()
            assert response_data.get("success") is False, "Должен быть success: false"
            # Проверка, содержит ли сообщение слово о неправильных данных
            assert "incorrect" in response_data.get("message", "").lower(), "Сообщение должно содержать информацию о неправильных данных"

    @allure.title("Попытка входа несуществующего пользователя")
    def test_login_nonexistent_user(self):
        api_client = StellarBurgersAPI()
        test_data = USER_TEST_DATA["invalid_login"]
        # Пытаемся войти как несуществующий пользователь
        with allure.step("Вход несуществующим пользователем"):
            response = api_client.login_user(test_data["email"], test_data["password"])
        
        # Проверка ошибки
        with allure.step("Проверка ошибки для несуществующего пользователя"):
            assert response.status_code == 401, f"Ожидалась ошибка 401, получен {response.status_code}"
            response_data = response.json()
            assert response_data.get("success") is False, "Должен быть success: false"
            assert "incorrect" in response_data.get("message", "").lower(), "Сообщение должно содержать информацию о неверных данных"