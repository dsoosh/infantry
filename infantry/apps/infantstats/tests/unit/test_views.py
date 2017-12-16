from django.test import TestCase
from django.urls import reverse

from infantry.apps.infantstats import urls


class StatisticsViewsTests(TestCase):
    def test__statistics_home_page_should_return_200_when_accessed(self):
        response = self.client.get(reverse(urls.base_url))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base.html")

