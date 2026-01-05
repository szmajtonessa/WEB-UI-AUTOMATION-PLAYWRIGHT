from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest

def test_inventory_page_elements(logged_in_page):


    inventory_page = InventoryPage(logged_in_page)
    
    assert len(inventory_page.get_inventory_items()) == 6
    
    assert inventory_page.cart_button.is_visible()
    
    assert inventory_page.menu_button.is_visible()

def test_logout(logged_in_page):


    inventory_page = InventoryPage(logged_in_page)
    
    inventory_page.logout()
    
    assert inventory_page.page.url == "https://www.saucedemo.com/"

def test_go_to_cart(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)

    inventory_page.go_to_cart()
    
    assert inventory_page.page.url.endswith("/cart.html")