from playwright.sync_api import Page


class RecoveryPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://omni.skroy.ru/recovery"  # Предполагаемый URL

        # Поля формы (аналогичны логину)
        self.email_input = page.locator('input[type="email"]')
        self.recover_button = page.locator('button:has-text("Восстановить")')
        self.login_link = page.locator('a:has-text("Войти")')
        self.register_link = page.locator('a:has-text("Зарегистрируйтесь")')

        # Сообщения
        self.success_message = page.locator('[role="status"]')
        self.error_message = page.locator('[role="alert"]')
        self.info_message = page.locator('.chakra-alert')  # Для информационных сообщений

        # Элементы для проверок
        self.email_label = page.locator('label:has-text("Email")')
        self.form_group = page.locator('div[role="group"].chakra-form-control')

    def navigate(self):
        """Открыть страницу восстановления"""
        self.page.goto(self.url)
        self.email_input.wait_for(state="visible", timeout=10000)

    def request_recovery(self, email: str):
        """Отправить запрос на восстановление"""
        self.email_input.fill(email)
        self.recover_button.click()

    def click_login_link(self):
        """Перейти на страницу логина"""
        self.login_link.click()
        self.page.wait_for_url("**/login", timeout=5000)

    def click_register_link(self):
        """Перейти на страницу регистрации"""
        self.register_link.click()
        self.page.wait_for_url("**/register", timeout=5000)

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

    def is_recovery_form_visible(self) -> bool:
        """Проверка видимости формы"""
        return self.email_input.is_visible() and self.recover_button.is_visible()