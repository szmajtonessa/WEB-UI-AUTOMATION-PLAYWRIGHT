from pages.checkout_two import checkout_two
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.checkout_one import checkout_one
from utils.test_data import URLS
from utils.test_data import PURCHASE_DATA

def test_checkout_finish(inventory_page_one_item):

    inventory_page = InventoryPage(inventory_page_one_item)
    inventory_page.go_to_cart()

    cart_page = CartPage(inventory_page_one_item)
    cart_page.proceed_to_checkout()

    checkout_page_one = checkout_one(inventory_page_one_item)
    checkout_page_one.checkout_info(PURCHASE_DATA["first_name"], PURCHASE_DATA["last_name"], PURCHASE_DATA["postal_code"])

    checkout_page_two = checkout_two(inventory_page_one_item)
    checkout_page_two.finish_checkout()

    assert checkout_page_two.page.url.endswith(URLS["checkout_complete_url"])

def test_checkout_cancel(inventory_page_one_item):

    inventory_page = InventoryPage(inventory_page_one_item)
    inventory_page.go_to_cart()

    cart_page = CartPage(inventory_page_one_item)
    cart_page.proceed_to_checkout()

    checkout_page_one = checkout_one(inventory_page_one_item)
    checkout_page_one.checkout_info(PURCHASE_DATA["first_name"], PURCHASE_DATA["last_name"], PURCHASE_DATA["postal_code"])

    checkout_page_two = checkout_two(inventory_page_one_item)
    checkout_page_two.cancel_checkout()

    assert checkout_page_two.page.url.endswith(URLS["inventory_url"])