import pytest
import time
from pages.register_page import RegisterPage


class TestRegister:

    @pytest.mark.smoke  # <-- Добавляем маркер
    @pytest.mark.register
    def test_register_page_elements_visibility(self, page):
        """Проверка всех элементов на странице регистрации"""
        register_page = RegisterPage(page)
        register_page.navigate()

        assert register_page.name_input.is_visible()
        assert register_page.email_input.is_visible()
        assert register_page.password_input.is_visible()
        assert register_page.confirm_password_input.is_visible()
        assert register_page.register_button.is_visible()
        assert register_page.login_link.is_visible()

    @pytest.mark.smoke  # <-- Добавляем маркер
    @pytest.mark.register
    def test_successful_registration(self, page):
        """Успешная регистрация нового пользователя"""
        register_page = RegisterPage(page)
        register_page.navigate()

        unique_email = f"test_{int(time.time())}_{int(time.time() * 1000)}@example.com"

        register_page.register(
            name="Test User",
            email=unique_email,
            password="TestPass123!",
            confirm_password="TestPass123!"
        )

        assert "login" in page.url or "success" in page.url
        assert register_page.success_message.is_visible(timeout=5000)

    @pytest.mark.register
    def test_registration_with_existing_email(self, page):
        """Регистрация с уже существующим email"""
        register_page = RegisterPage(page)
        register_page.navigate()

        register_page.register(
            name="Test User",
            email="existing@example.com",
            password="TestPass123!",
            confirm_password="TestPass123!"
        )

        error_text = register_page.get_error_text()
        assert "существует" in error_text.lower() or "используется" in error_text.lower()

    @pytest.mark.register
    def test_password_mismatch(self, page):
        """Проверка несовпадения паролей"""
        register_page = RegisterPage(page)
        register_page.navigate()

        register_page.register(
            name="Test User",
            email="test@example.com",
            password="Password123!",
            confirm_password="Different123!"
        )

        error_text = register_page.get_error_text()
        assert "совпадают" in error_text.lower() or "пароль" in error_text.lower()

    @pytest.mark.register
    def test_register_with_empty_fields(self, page):
        """Проверка валидации пустых полей"""
        register_page = RegisterPage(page)
        register_page.navigate()

        register_page.register_button.click()

        assert register_page.name_input.get_attribute("required") is not None
        assert register_page.email_input.get_attribute("required") is not None
        assert register_page.password_input.get_attribute("required") is not None
        assert register_page.confirm_password_input.get_attribute("required") is not None

    @pytest.mark.register
    def test_login_link_from_register_page(self, page):
        """Переход на страницу логина со страницы регистрации"""
        register_page = RegisterPage(page)
        register_page.navigate()
        register_page.click_login_link()

        assert "login" in page.url
        assert page.locator('button:has-text("Войти")').is_visible()

    # Параметризованные тесты для имени
    @pytest.mark.parametrize("name,is_valid", [
        ("John", True),
        ("Иван Петров", True),
        ("John Doe", True),
        ("J", False),
        ("", False),
        ("A" * 100, False),
        ("John@Doe", False),
        ("12345", False),
    ])
    @pytest.mark.register
    def test_name_validation(self, page, name, is_valid):
        """Проверка валидации поля имени"""
        register_page = RegisterPage(page)
        register_page.navigate()

        register_page.name_input.fill(name)
        register_page.email_input.fill("test@example.com")
        register_page.password_input.fill("TestPass123!")
        register_page.confirm_password_input.fill("TestPass123!")
        register_page.register_button.click()

        validity = register_page.name_input.evaluate("el => el.validity")
        if is_valid:
            assert validity["valid"] is True
        else:
            assert validity["valid"] is False

    # Параметризованные тесты для email
    @pytest.mark.parametrize("email,is_valid", [
        ("test@example.com", True),
        ("user.name@domain.co.uk", True),
        ("test@sub.domain.com", True),
        ("test@example", False),
        ("test.example.com", False),
        ("test@.com", False),
        ("", False),
    ])
    @pytest.mark.register
    def test_email_validation(self, page, email, is_valid):
        """Проверка валидации поля email"""
        register_page = RegisterPage(page)
        register_page.navigate()

        register_page.name_input.fill("Test User")
        register_page.email_input.fill(email)
        register_page.password_input.fill("TestPass123!")
        register_page.confirm_password_input.fill("TestPass123!")
        register_page.register_button.click()

        validity = register_page.email_input.evaluate("el => el.validity")
        if is_valid:
            assert validity["valid"] is True
        else:
            assert validity["valid"] is False

    # Параметризованные тесты для пароля
    @pytest.mark.parametrize("password,is_valid", [
        ("TestPass123!", True),
        ("TestPass123", False),
        ("testpass123!", False),
        ("TESTPASS123!", False),
        ("TestPass!", False),
        ("12345678", False),
        ("Test", False),
        ("TestPass123!@#$%^&*()", True),
        ("", False),
    ])
    @pytest.mark.register
    def test_password_complexity(self, page, password, is_valid):
        """Проверка сложности пароля"""
        register_page = RegisterPage(page)
        register_page.navigate()

        register_page.name_input.fill("Test User")
        register_page.email_input.fill("test@example.com")
        register_page.password_input.fill(password)
        register_page.confirm_password_input.fill(password)
        register_page.register_button.click()

        validity = register_page.password_input.evaluate("el => el.validity")
        if is_valid:
            assert validity["valid"] is True
        else:
            assert validity["valid"] is False

    @pytest.mark.register
    def test_password_visibility_toggle(self, page):
        """Проверка переключения видимости пароля (если есть)"""
        register_page = RegisterPage(page)
        register_page.navigate()

        toggle_button = page.locator('button[aria-label*="показать"]').first
        if toggle_button.is_visible():
            assert register_page.password_input.get_attribute("type") == "password"
            toggle_button.click()
            assert register_page.password_input.get_attribute("type") == "text"

    @pytest.mark.register
    def test_register_form_reset_after_error(self, page):
        """Проверка, что форма не сбрасывается после ошибки"""
        register_page = RegisterPage(page)
        register_page.navigate()

        name = "Test User"
        email = "test@example.com"
        register_page.name_input.fill(name)
        register_page.email_input.fill(email)

        register_page.password_input.fill("123")
        register_page.confirm_password_input.fill("123")
        register_page.register_button.click()

        assert register_page.name_input.input_value() == name
        assert register_page.email_input.input_value() == email

    @pytest.mark.register
    def test_max_length_validation(self, page):
        """Проверка максимальной длины полей"""
        register_page = RegisterPage(page)
        register_page.navigate()

        max_length_name = register_page.name_input.get_attribute("maxlength")
        if max_length_name:
            long_name = "A" * (int(max_length_name) + 1)
            register_page.name_input.fill(long_name)
            assert len(register_page.name_input.input_value()) <= int(max_length_name)