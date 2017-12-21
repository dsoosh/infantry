import pytest
from django.urls import reverse
from selenium.webdriver.chrome.webdriver import WebDriver

from ..fixtures import paths
from ... import urls


@pytest.fixture
def browser():
    driver = WebDriver()
    yield driver
    driver.quit()


def live_reverse(server, url):
    return f"{server.url}" + reverse(url)


@pytest.mark.ui
def test_access_statistics_page(live_server, browser):
    browser.get(live_reverse(live_server, urls.base_url))
    assert browser.title == "Statistics"


@pytest.mark.ui
def test_upload_source_database_using_web_form(live_server, browser):
    browser.get(live_reverse(live_server, urls.upload_url))
    upload_input = browser.find_element_by_name("database")
    upload_input.send_keys(paths.database)
    submit = browser.find_element_by_name("upload")
    submit.click()
    assert browser.current_url == live_reverse(live_server, urls.base_url)
