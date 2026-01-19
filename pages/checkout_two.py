from playwright.sync_api import Page

class checkout_two:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.locator("button#finish")
        self.cancel_button = page.locator("button#cancel")
        

    def finish_checkout(self):
        self.finish_button.click()

    def cancel_checkout(self):
        self.cancel_button.click()
