from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("button#checkout")
        self.continue_shopping_button = page.locator("button#continue-shopping")
        self.remove_item_button = page.locator("button.btn_secondary.btn_small.cart_button")
    
    def get_cart_items(self):
        return self.cart_items.all()
    
    def proceed_to_checkout(self):
        self.checkout_button.click()
    
    def continue_shopping(self):
        self.continue_shopping_button.click()

    def remove_item(self):
        self.remove_item_button.click()