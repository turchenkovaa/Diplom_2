# Тестовые данные для пользователей
USER_TEST_DATA = {
    # Пользователь с пропущенным email
    "missing_email": {
        "email": "",
        "password": "password123",
        "name": "Test User"
    },
    # Пользователь с пропущенным паролем
    "missing_password": {
        "email": "test@test.com",
        "password": "",
        "name": "Test User"
    },
    # Пользователь с пропущенным именем
    "missing_name": {
        "email": "test@test.com",
        "password": "password123",
        "name": ""
    },
    # Уже существующий пользователь (для проверки регистрации или дублирующихся данных)
    "existing_user": {
        "email": "existing_user@test.com",
        "password": "password123",
        "name": "Existing User"
    },
    # Невалидный логин (несуществующий пользователь или неправильный пароль)
    "invalid_login": {
        "email": "nonexistent@test.com",
        "password": "wrongpassword"
    }
}

# Тестовые данные для заказов
ORDER_TEST_DATA = {
    # Валидный список ингредиентов
    "valid_ingredients": ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"],
    # Неверные или несуществующие хеши ингредиентов
    "invalid_ingredients": ["invalid_hash_123", "another_invalid_hash"],
    # Пустой список ингредиентов
    "empty_ingredients": []
}