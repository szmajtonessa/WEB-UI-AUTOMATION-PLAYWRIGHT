from pages.checkout_one import checkout_one
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
import pytest
from utils.test_data import URLS
from utils.test_data import PURCHASE_DATA

def test_valid_checkout_info(inventory_page_one_item):

    inventory_page = InventoryPage(inventory_page_one_item)
    inventory_page.go_to_cart()

    cart_page = CartPage(inventory_page_one_item)
    cart_page.proceed_to_checkout()

    checkout_page = checkout_one(inventory_page_one_item)
    checkout_page.checkout_info(PURCHASE_DATA["first_name"], PURCHASE_DATA["last_name"], PURCHASE_DATA["postal_code"])

    assert checkout_page.page.url.endswith(URLS["checkout_step_two_url"])

@pytest.mark.parametrize("first_name, last_name, postal_code, error_message", [
    ("", "Doe", "12345", "Error: First Name is required"),
    ("John", "", "12345", "Error: Last Name is required"),
    ("John", "Doe", "", "Error: Postal Code is required"),
])

def test_invalid_checkout_info(inventory_page_one_item, first_name, last_name, postal_code, error_message):

    inventory_page = InventoryPage(inventory_page_one_item)
    inventory_page.go_to_cart()

    cart_page = CartPage(inventory_page_one_item)
    cart_page.proceed_to_checkout()

    checkout_page = checkout_one(inventory_page_one_item)
    checkout_page.checkout_info(first_name, last_name, postal_code)
    
    assert checkout_page.error_message.is_visible()
    assert checkout_page.error_message.text_content() == error_message