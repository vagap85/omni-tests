from playwright.sync_api import Page


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        # ПРАВИЛЬНЫЙ URL!
        self.url = "https://omni.skroy.ru/registration"

        # Поля формы (из теста)
        self.email_input = page.locator('input[placeholder="example@omninotice"]')
        self.password_input = page.locator('input[placeholder="введите пароль"]')
        self.confirm_password_input = page.locator('input[placeholder="повторите пароль"]')

        # Кнопки
        self.register_button = page.locator('button:has-text("Создать аккаунт")')
        self.home_button = page.locator('button:has-text("На главную")')

        # Сообщения
        self.error_message = page.locator('[role="alert"]')
        self.success_message = page.locator('[role="status"]')

        # Логотип (если есть)
        self.logo = page.locator('img[alt="OmniNotice"]')

    def navigate(self):
        """Открыть страницу регистрации"""
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")
        self.email_input.wait_for(state="visible", timeout=10000)

    def register(self, email: str, password: str, confirm_password: str = None):
        """Заполнить форму регистрации"""
        if not confirm_password:
            confirm_password = password

        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)
        self.register_button.click()

    def click_home_button(self):
        """Перейти на главную"""
        self.home_button.click()
        self.page.wait_for_url("**/", timeout=5000)

    def get_error_text(self) -> str:
        """Получить текст ошибки"""
        if self.error_message.is_visible():
            return self.error_message.text_content()
        return ""

    def get_success_text(self) -> str:
        """Получить текст успешного сообщения"""
        if self.success_message.is_visible():
            return self.success_message.text_content()
        return ""