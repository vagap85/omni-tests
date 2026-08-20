from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://omni.skroy.ru/login"

        # Поля формы
        self.login_input = page.locator('input[placeholder="example@omninotice"]')
        self.password_input = page.locator('input[placeholder="введите пароль"]')
        self.submit_button = page.locator('button:has-text("Войти")')
        self.register_link = page.locator('a:has-text("Зарегистрируйтесь")')
        self.home_button = page.locator('button:has-text("На главную")')

        # Chakra UI элементы
        self.error_message = page.locator('[role="alert"]')
        self.success_message = page.locator('[role="status"]')
        self.logo = page.locator('img[alt="OmniNotice"]')

    def navigate(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")
        self.login_input.wait_for(state="visible", timeout=10000)

    def login(self, login: str, password: str):
        self.login_input.click()
        self.login_input.fill(login)
        self.password_input.click()
        self.password_input.fill(password)
        self.submit_button.click()

    def click_register_link(self):
        self.register_link.click()
        self.page.wait_for_url(lambda url: "register" in url or "registration" in url, timeout=5000)

    def click_home_button(self):
        self.home_button.click()
        self.page.wait_for_url("**/", timeout=5000)

    def get_error_text(self) -> str:
        if self.error_message.is_visible():
            return self.error_message.text_content()
        return ""

    def is_login_form_visible(self) -> bool:
        return self.login_input.is_visible() and self.password_input.is_visible()