from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest

def test_goto_checkout_one(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.go_to_cart()
    
    cart_page = CartPage(logged_in_page)
    cart_page.proceed_to_checkout()
    
    assert cart_page.page.url.endswith("/checkout-step-one.html")

#def test_cart_remove_items(logged_in_page)