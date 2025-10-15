import random
import string
from datetime import datetime

# ----------------------------------------
# Функции для генерации случайных данных для тестирования
# ----------------------------------------

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_unique_email():
    # Получение метки времени в формате ГГГГММДДЧЧММСС
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # Генерация случайной строки из 6 букв
    random_str = ''.join(random.choices(string.ascii_lowercase, k=6))
    # Формирование email
    return f"test_{timestamp}_{random_str}@test.com"