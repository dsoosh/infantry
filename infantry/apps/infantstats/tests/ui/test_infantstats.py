from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class InfantStatsUITests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test__access_the_statistics_page__should_return_200(self):
        self.browser.get(f'{self.live_server_url}/statistics')
        self.assertEqual(self.browser.title, "Statistics")

