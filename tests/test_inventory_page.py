from playwright.sync_api._generated import Page
from pages.inventory_page import InventoryPage
from utils.test_data import URLS


def test_inventory_page_elements(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    
    assert inventory_page.is_loaded()
    assert inventory_page.cart_button.is_visible()
    assert inventory_page.menu_button.is_visible()

def test_logout(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.logout()
    
    assert "saucedemo.com" in inventory_page.page.url

def test_go_to_cart(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.go_to_cart()
    
    assert inventory_page.page.url.endswith(URLS["cart_url"])

def test_add_to_cart(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart()
    
    assert inventory_page.page.locator("span.shopping_cart_badge").is_visible()

def test_remove_from_cart(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart()
    
    assert inventory_page.page.locator("span.shopping_cart_badge").is_visible()

    inventory_page.remove_from_cart()
    
    assert not inventory_page.page.locator("span.shopping_cart_badge").is_visible()