import time


def test_open_site(website_app):
    website_app.navigate_to_site()
    # test
    website_app.choose_store_page.choose_de_store()
    website_app.home_page.choose_hairloss_category()
    website_app.common.accept_cookies()


def test_cookie_on_the_cat_page(website_app):
    website_app.navigate_to_site(endpoint='/de/produkt-kategorie/maennergesundheit/erektile-dysfunktion')
    website_app.common.accept_cookies()
