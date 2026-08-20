import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_page_loads(page):
    """Проверка загрузки страницы логина"""
    login_page = LoginPage(page)
    login_page.navigate()

    assert "login" in page.url
    assert login_page.login_input.is_visible()
    assert login_page.password_input.is_visible()
    assert login_page.submit_button.is_visible()
    print("✅ Страница логина загружена!")


@pytest.mark.smoke
def test_login_page_has_logo(page):
    """Проверка наличия логотипа"""
    login_page = LoginPage(page)
    login_page.navigate()

    assert login_page.logo.is_visible()
    print("✅ Логотип виден!")


@pytest.mark.smoke
def test_login_page_has_register_link(page):
    """Проверка наличия ссылки на регистрацию"""
    login_page = LoginPage(page)
    login_page.navigate()

    assert login_page.register_link.is_visible()
    print("✅ Ссылка на регистрацию видна!")