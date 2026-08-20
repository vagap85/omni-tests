from playwright.sync_api import Page


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://omni.skroy.ru/register"

        # Поля формы (аналогичны логину, но с другими placeholder)
        self.name_input = page.locator('input[placeholder*="Имя"]').first
        self.email_input = page.locator('input[placeholder*="email"]').first
        self.password_input = page.locator('input[placeholder*="пароль"]').first
        self.confirm_password_input = page.locator('input[placeholder*="подтвердите"]').first
        self.register_button = page.locator('button:has-text("Зарегистрироваться")')
        self.login_link = page.locator('a:has-text("Войти")')

        self.error_message = page.locator('[role="alert"]')
        self.success_message = page.locator('[role="status"]')

    def navigate(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")
        self.name_input.wait_for(state="visible", timeout=10000)

    def register(self, name: str, email: str, password: str, confirm_password: str = None):
        if not confirm_password:
            confirm_password = password

        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)
        self.register_button.click()