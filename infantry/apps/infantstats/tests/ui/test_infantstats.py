import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def browser():
    driver = WebDriver()
    yield driver
    driver.quit()


@pytest.mark.ui
def test_access_statistics_page(live_server, browser):
    browser.get(f'{live_server.url}/statistics')
    assert browser.title == "Statistics"
