import pytest
from django.urls import reverse

from infantry.apps.infantstats import urls


@pytest.mark.django_db
def test_statistics_page_returns_200(client):
    response = client.get(reverse(urls.base_url))
    assert response.status_code == 200
    assert "base.html" in [template.name for template in response.templates]
