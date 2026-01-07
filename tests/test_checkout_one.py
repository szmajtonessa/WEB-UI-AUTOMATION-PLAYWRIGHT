from pages.checkout_one import checkout_one
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
import pytest

def test_valid_checkout_info(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.go_to_cart()
    
    cart_page = CartPage(logged_in_page)
    cart_page.proceed_to_checkout()
    
    checkout_page = checkout_one(logged_in_page)
    checkout_page.checkout_info(first_name="John", last_name="Doe", postal_code="12345")
    
    assert checkout_page.page.url.endswith("/checkout-step-two.html")

@pytest.mark.parametrize("first_name, last_name, postal_code, error_message", [
    ("", "Doe", "12345", "Error: First Name is required"),
    ("John", "", "12345", "Error: Last Name is required"),
    ("John", "Doe", "", "Error: Postal Code is required"),
])

def test_invalid_checkout_info(logged_in_page, first_name, last_name, postal_code, error_message):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.go_to_cart()
    
    cart_page = CartPage(logged_in_page)
    cart_page.proceed_to_checkout()
    
    checkout_page = checkout_one(logged_in_page)
    checkout_page.checkout_info(first_name, last_name, postal_code)
    
    assert checkout_page.error_message.is_visible()
    assert checkout_page.error_message.text_content() == error_message