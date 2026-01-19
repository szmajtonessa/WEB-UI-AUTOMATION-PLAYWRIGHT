from playwright.sync_api import Page

class CompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.back_home_button = page.locator("button#back-to-products")

    def back_to_home(self):
        self.back_home_button.click()