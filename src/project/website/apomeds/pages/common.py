import allure
from playwright.sync_api import Page


class Common(object):
    def __init__(self, page: Page):
        self.page = page

    @allure.step('cookie accept')
    def accept_cookies(self):
        self.page.click('id=accept_cookie')
