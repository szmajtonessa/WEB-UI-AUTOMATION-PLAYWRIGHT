from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.test_data import URLS


def test_goto_checkout_one(inventory_page_one_item):

    inventory_page = InventoryPage(inventory_page_one_item)
    inventory_page.go_to_cart()

    cart_page = CartPage(inventory_page_one_item)
    cart_page.proceed_to_checkout()
    
    assert cart_page.page.url.endswith(URLS["checkout_step_one_url"])

def test_continue_shopping(inventory_page_one_item):

    inventory_page = InventoryPage(inventory_page_one_item)
    inventory_page.go_to_cart()

    cart_page = CartPage(inventory_page_one_item)
    cart_page.continue_shopping()
    
    assert cart_page.page.url.endswith(URLS["inventory_url"])

def test_cart_remove_item(inventory_page_one_item):

    inventory_page = InventoryPage(inventory_page_one_item)
    inventory_page.go_to_cart()

    cart_page = CartPage(inventory_page_one_item)
    cart_page.remove_item()
    
    assert cart_page.cart_items.count() == 0