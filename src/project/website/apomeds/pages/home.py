import allure
from playwright.sync_api import Page


class HomePage(object):
    def __init__(self, page: Page):
        self.page = page

    @allure.step('click on the hair loss category')
    def choose_hairloss_category(self):
        self.page.click('id=32')
