from playwright.sync_api import Page

class checkout_one:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_box = page.locator("input#first-name")
        self.last_name_box = page.locator("input#last-name")
        self.postal_code_box = page.locator("input#postal-code")
        self.continue_button = page.locator("input#continue")
        self.cancel_button = page.locator("button#cancel")
        self.error_message = page.locator("h3[data-test='error']")


    def checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_box.fill(first_name)
        self.last_name_box.fill(last_name)
        self.postal_code_box.fill(postal_code)
        self.continue_button.click()

    def cancel_checkout(self):
        self.cancel_button.click()