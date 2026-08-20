import pytest
import allure
from pages.login_page import LoginPage
from config import Config


@allure.feature("Авторизация")
@allure.story("Логин пользователя")
class TestLogin:

    @allure.title("Проверка всех элементов на странице логина")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.login
    def test_login_page_elements_visibility(self, page):
        """Проверка всех элементов на странице логина"""
        with allure.step("Открыть страницу логина"):
            login_page = LoginPage(page)
            login_page.navigate()

        with allure.step("Проверить наличие всех элементов"):
            assert login_page.login_input.is_visible()
            assert login_page.password_input.is_visible()
            assert login_page.submit_button.is_visible()
            assert login_page.register_link.is_visible()
            assert login_page.logo.is_visible()

        allure.attach(page.screenshot(), name="Страница логина", attachment_type=allure.attachment_type.PNG)
        print("✅ Все элементы страницы логина видны")