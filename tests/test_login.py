import pytest
from pages.login_page import LoginPage
from config import Config


class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.login
    def test_login_page_elements_visibility(self, page):
        """Проверка всех элементов на странице логина"""
        login_page = LoginPage(page)
        login_page.navigate()

        assert login_page.login_input.is_visible()
        assert login_page.password_input.is_visible()
        assert login_page.submit_button.is_visible()
        assert login_page.register_link.is_visible()
        assert login_page.logo.is_visible()
        print("✅ Все элементы страницы логина видны")

    @pytest.mark.smoke
    @pytest.mark.login
    def test_login_with_valid_credentials(self, page):
        """Успешная авторизация с реальным пользователем"""
        login_page = LoginPage(page)
        login_page.navigate()

        # Используем данные из .env
        login_page.login(Config.TEST_USER_LOGIN, Config.TEST_USER_PASSWORD)

        # Ждем редиректа или загрузки страницы
        page.wait_for_timeout(3000)

        # Проверяем, что ушли со страницы логина
        assert "login" not in page.url, "Не удалось войти - остались на странице логина"
        print(f"✅ Успешный вход! Текущий URL: {page.url}")

        # Проверяем, что на странице есть какой-то контент
        page_content = page.content()
        assert len(page_content) > 0, "Страница пуста после входа"

    @pytest.mark.login
    def test_login_with_invalid_credentials(self, page):
        """Вход с неверными данными"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("wrong@example.com", "wrongpass")

        page.wait_for_timeout(2000)
        # Должны остаться на странице логина
        assert "login" in page.url
        print("✅ Остались на странице логина с неверными данными")

    @pytest.mark.login
    def test_login_with_empty_fields(self, page):
        """Проверка валидации пустых полей"""
        login_page = LoginPage(page)
        login_page.navigate()

        # Кликаем на кнопку без заполнения
        login_page.submit_button.click()

        # Проверяем, что поля требуют заполнения
        is_required = login_page.login_input.evaluate("el => el.required")
        assert is_required is True
        print("✅ Поля требуют заполнения")

    @pytest.mark.login
    def test_register_link_navigation(self, page):
        """Проверка перехода на страницу регистрации"""
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.click_register_link()

        assert "login" not in page.url
        print(f"✅ Переход на страницу: {page.url}")

    @pytest.mark.login
    def test_home_button_navigation(self, page):
        """Проверка перехода на главную страницу"""
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.click_home_button()

        assert "login" not in page.url
        print(f"✅ Переход на главную: {page.url}")