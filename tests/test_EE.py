from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_one import checkout_one
from pages.checkout_two import checkout_two
from pages.complete_page import CompletePage
from utils.test_data import USERS
from utils.test_data import URLS
from utils.test_data import PURCHASE_DATA

def test_end_to_end_purchase(page):
    
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(USERS["standard_user"]["username"], USERS["standard_user"]["password"])

    assert login_page.page.url.endswith(URLS["inventory_url"])

    
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    assert inventory_page.page.url.endswith(URLS["cart_url"])
    

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    assert cart_page.page.url.endswith(URLS["checkout_step_one_url"])

    
    checkout_page_one = checkout_one(page)
    checkout_page_one.checkout_info(PURCHASE_DATA["first_name"], PURCHASE_DATA["last_name"], PURCHASE_DATA["postal_code"])

    assert checkout_page_one.page.url.endswith(URLS["checkout_step_two_url"])
    

    checkout_page_two = checkout_two(page)
    checkout_page_two.finish_checkout()

    assert checkout_page_two.page.url.endswith(URLS["checkout_complete_url"])
    

    complete_page = CompletePage(page)
    complete_page.back_to_home()

    assert complete_page.page.url.endswith(URLS["inventory_url"])