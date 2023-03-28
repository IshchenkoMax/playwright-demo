from playwright.sync_api import Page


class HomePage(object):
    def __init__(self, page: Page):
        self.page = page

    def choose_hairloss_category(self):
        self.page.click('id=32')
