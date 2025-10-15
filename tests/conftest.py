import pytest
import allure
from api_client.api_client import StellarBurgersAPI
from help.generator import generate_unique_email
from help.data import USER_TEST_DATA

# ----------------------------------------
# Фикстуры для тестирования API Stellar Burgers
# ----------------------------------------

@pytest.fixture
def user_data():
    # Возвращает словарь с тестовыми данными пользователя
    # Email генерируется уникальный для каждого теста
    return {
        "email": generate_unique_email(),
        "password": "password123",
        "name": "Test User",
    }

@pytest.fixture
def create_and_delete_user():
    # Создает пользователя перед тестом и удаляет после
    api_client = StellarBurgersAPI()
    
    with allure.step("Создаем пользователя"):
        email = generate_unique_email()
        password = "password123"
        name = "Test User"
        
    yield api_client, email, password, name

    with allure.step("Удаляем пользователя"):
        if api_client.token:
            api_client.delete_user()

@pytest.fixture
def authenticated_user():
    # Регистрирует и логинит пользователя, возвращает авторизованный API клиент
    api_client = StellarBurgersAPI()
    
    with allure.step("Регистрация и логин пользователя"):
        email = generate_unique_email()
        password = "password123"
        name = "Test User"

        api_client.register_user(email, password, name)
        api_client.login_user(email, password)
        
    yield api_client

    with allure.step("Удаляем пользователя"):
        if api_client.token:
            api_client.delete_user()