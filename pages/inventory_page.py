from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator("div.inventory_item_name")
        self.cart_button = page.locator("a.shopping_cart_link")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.locator("[data-test=\"logout-sidebar-link\"]")

    def open(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def get_inventory_items(self):
        return self.inventory_items.all_text_contents()

    def go_to_cart(self):
        self.cart_button.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()