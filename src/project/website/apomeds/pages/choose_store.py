import allure
from playwright.sync_api import Page


class ChooseStore(object):
    def __init__(self, page: Page):
        self.page = page

    @allure.step('click on the de store tile')
    def choose_de_store(self):
        try:
            el = self.page.locator('id=de')
            screen = self.page.screenshot(path='allure-results/test_screen1.png', full_page=True)
            allure.attach(screen, attachment_type=allure.attachment_type.PNG)
        except Exception:
            print('ERROR')
            screen = self.page.screenshot(path='allure-results/test_screen.png', full_page=True)
            allure.attach(screen, attachment_type=allure.attachment_type.PNG)
            raise
        el.click()
