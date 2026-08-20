import pytest
import os
from playwright.sync_api import Page, BrowserContext
from datetime import datetime


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """Создает новую страницу для каждого теста"""
    page = context.new_page()
    page.set_default_timeout(10000)
    page.on("pageerror", lambda err: None)
    yield page
    page.close()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Настройки контекста"""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }


def pytest_configure(config):
    """Добавляем кастомные маркеры"""
    config.addinivalue_line("markers", "smoke: Быстрые тесты для проверки основных функций")
    config.addinivalue_line("markers", "regression: Полный регрессионный набор")
    config.addinivalue_line("markers", "login: Тесты авторизации")
    config.addinivalue_line("markers", "register: Тесты регистрации")
    config.addinivalue_line("markers", "recovery: Тесты восстановления пароля")
    config.addinivalue_line("markers", "debug: Отладочные тесты")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Делаем скриншот при падении теста"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "page" in item.fixturenames:
            page = item.funcargs["page"]

            # Создаем папку для скриншотов
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # Сохраняем скриншот с именем теста и временем
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"{screenshots_dir}/failed_{item.name}_{timestamp}.png"

            try:
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"\n📸 Скриншот сохранен: {screenshot_path}")
            except Exception as e:
                print(f"\n⚠️ Не удалось сохранить скриншот: {e}")