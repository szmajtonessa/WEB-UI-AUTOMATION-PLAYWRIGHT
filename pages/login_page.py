from playwright.sync_api import Page
from utils.test_data import URLS

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.locator("input#user-name")
        self.password_input = page.locator("input#password")
        self.login_button = page.locator("input#login-button")
        self.error_message = page.locator("h3[data-test='error']")

    def open(self):
        self.page.goto(URLS["base_url"])

    def login(self, username: str, password: str):
        
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
          