import pytest

from src.helpers.common_helpers import url_parser_query


@pytest.mark.base
def test_open_site_1(website_app):
    website_app.navigate_to_site()


@pytest.mark.other
@pytest.mark.base
def test_open_site_2(website_app):
    website_app.navigate_to_site()


@pytest.mark.base
def test_open_site_3(website_app):
    website_app.navigate_to_site()


@pytest.mark.base
def test_open_site_4(website_app):
    website_app.navigate_to_site()


def test_open_site_5(website_app):
    website_app.navigate_to_site()


def test_open_site_6(website_app):
    website_app.navigate_to_site()


def test_open_site_7(website_app):
    website_app.navigate_to_site()


def test_open_site_9(website_app):
    website_app.navigate_to_site()


@pytest.mark.skip('AS-0000')
def test_open_custom_link(website_app):
    website_app.navigate_to_site(custom='https://ggooooogle.com.ua')


def test_123(website_app):
    url = 'https://apomeds.com/de/produkt/biotin-5000-gummis?qty=1&type=subscription&sp=3_month'
    result = url_parser_query(url, 'sp')
    print(result)
