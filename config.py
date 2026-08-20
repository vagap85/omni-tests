import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()


class Config:
    """Конфигурация для тестов"""

    # Тестовые данные
    TEST_USER_LOGIN = os.getenv("TEST_USER_LOGIN", "q@q.co")
    TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD", "q")
    TEST_USER_NAME = os.getenv("TEST_USER_NAME", "Test User")
    BASE_URL = os.getenv("BASE_URL", "https://omni.skroy.ru")

    # Настройки Playwright
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))