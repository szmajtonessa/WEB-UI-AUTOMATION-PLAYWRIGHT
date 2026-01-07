from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator("div.inventory_item_name")
        self.cart_button = page.locator("a.shopping_cart_link")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.locator("[data-test=\"logout-sidebar-link\"]")
        self.add_to_cart_buttons = page.locator("[data-test^=\"add-to-cart-\"]")
        self.add_to_cart_backpack_button = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.remove_backpack_from_cart_button = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")
        
        

    def is_loaded(self):
        return self.inventory_items.first.is_visible()

    def go_to_cart(self):
        self.cart_button.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()
    
    def add_to_cart(self):
        self.add_to_cart_backpack_button.click()

    def remove_from_cart(self):
        if self.remove_backpack_from_cart_button.is_visible():
            self.remove_backpack_from_cart_button.click()

    # def add_to_cart(self):
    #     while self.add_to_cart_buttons.count() > 0:
    #         self.add_to_cart_buttons.first.click()
        