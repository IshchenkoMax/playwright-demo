from playwright.sync_api import Page


class ChooseStore(object):
    def __init__(self, page: Page):
        self.page = page

    def choose_de_store(self):
        self.page.click('id=de')
