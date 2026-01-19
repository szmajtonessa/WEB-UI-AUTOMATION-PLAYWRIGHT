import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import USERS
import os

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser: Browser):
    context = browser.new_context(
        record_video_dir="reports/videos"
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    yield page

    
    context.close()


@pytest.fixture
def logged_in_page(page):
    logged_in_page = LoginPage(page)
    logged_in_page.open()
    logged_in_page.login(USERS["standard_user"]["username"], USERS["standard_user"]["password"])
    return page

@pytest.fixture
def inventory_page_one_item(page):
    logged_in_page = LoginPage(page)
    logged_in_page.open()
    logged_in_page.login(USERS["standard_user"]["username"], USERS["standard_user"]["password"])

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart()
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            os.makedirs("reports/traces", exist_ok=True)

            page.screenshot(
                path=f"reports/screenshots/{item.name}.png"
            )

            page.context.tracing.stop(
                path=f"reports/traces/{item.name}.zip"
            )
