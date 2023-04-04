from playwright.sync_api import Page

from src.project.website.apomeds.pages.choose_store import ChooseStore
from src.project.website.apomeds.pages.common import Common
from src.project.website.apomeds.pages.home import HomePage


class WebsiteApp:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_site(self, endpoint: str = False, qry: str = False, custom: str = False):
        base_url = 'https://apomeds.com'
        if endpoint:
            self.page.goto(base_url + endpoint)
        elif endpoint and qry:
            self.page.goto(base_url + endpoint + qry)
        elif custom:
            self.page.goto(custom)
        else:
            self.page.goto(base_url)

    @property
    def choose_store_page(self):
        return ChooseStore(self.page)

    @property
    def home_page(self):
        return HomePage(self.page)

    @property
    def common(self):
        return Common(self.page)
