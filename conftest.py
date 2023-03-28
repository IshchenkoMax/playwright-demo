import pytest
from playwright.sync_api import Browser

from src.project.website.website_app import WebsiteApp


@pytest.fixture
def website_app(browser: Browser):
    page = browser.new_page()
    yield WebsiteApp(page)
