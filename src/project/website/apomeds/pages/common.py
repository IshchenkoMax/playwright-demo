from playwright.sync_api import Page


class Common(object):
    def __init__(self, page: Page):
        self.page = page

    def accept_cookies(self):
        self.page.click('id=accept_cookie')
