from pages.login_page import LoginPage
import pytest
from utils.test_data import URLS

def test_valid_login(logged_in_page):

    login_page = LoginPage(logged_in_page)

    assert login_page.page.url.endswith(URLS["inventory_url"])
    
@pytest.mark.parametrize("username, password, error_message", [
    ("", "", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("invalid_user", "invalid_pass", "Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")
])

def test_invalid_login(page, username, password, error_message):

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
        
    assert login_page.error_message.is_visible()
    assert login_page.error_message.text_content() == error_message