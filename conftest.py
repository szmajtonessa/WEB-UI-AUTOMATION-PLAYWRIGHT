import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from pages.login_page import LoginPage
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser: Browser):
    
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def logged_in_page(page):
    logged_in_page = LoginPage(page)
    logged_in_page.open()
    logged_in_page.login("standard_user", "secret_sauce")
    return page
