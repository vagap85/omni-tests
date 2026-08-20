import pytest
from pages.login_page import LoginPage
from config import Config


class TestLoginParametrized:

    @pytest.mark.parametrize("login,password,expected_result", [
        (Config.TEST_USER_LOGIN, Config.TEST_USER_PASSWORD, "success"),  # Валидные данные
        ("q@q.co", "wrong", "fail"),  # Неверный пароль
        ("wrong@example.com", "q", "fail"),  # Неверный логин
        ("", "q", "fail"),  # Пустой логин
        ("q@q.co", "", "fail"),  # Пустой пароль
    ])
    @pytest.mark.login
    def test_login_scenarios(self, page, login, password, expected_result):
        """Проверка различных сценариев входа"""
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(login, password)
        page.wait_for_timeout(2000)

        if expected_result == "success":
            assert "login" not in page.url, f"Не удалось войти с данными: {login}/{password}"
            print(f"✅ Успешный вход с {login}")
        else:
            assert "login" in page.url, f"Неожиданно удалось войти с {login}/{password}"
            print(f"✅ Вход отклонен для {login}")