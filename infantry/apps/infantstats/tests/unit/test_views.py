from io import BytesIO

import pytest
from django.urls import reverse

from ..fixtures import paths
from ... import urls


@pytest.mark.django_db
def test_load_statistics_home_page(client):
    response = client.get(reverse(urls.base_url))
    assert response.status_code == 200
    assert "base.html" in [template.name for template in response.templates]


@pytest.mark.django_db
def test_load_source_db_upload_page(client):
    response = client.get(reverse(urls.upload_url))
    assert response.status_code == 200
    assert "upload.html" in [template.name for template in response.templates]


@pytest.mark.django_db
def test_valid_database_file_upload(client):
    with open(paths.database, "rb") as db_file:
        response = client.post(reverse(urls.upload_url), {"database": db_file}, format="multipart")
        assert response.status_code == 302
        assert response.get('Location') == reverse(urls.base_url)


@pytest.mark.django_db
def test_invalid_database_file_upload(client):
    bad_db = BytesIO(b"data")

    response = client.post(reverse(urls.upload_url), {"database": bad_db}, format="multipart")
    form = response.context["form"]

    assert response.status_code == 200
    assert form.errors is not None
    assert "This is not a sqlite3 database file" in form.errors["database"]
