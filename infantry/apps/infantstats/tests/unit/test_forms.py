from django.core.files.uploadedfile import SimpleUploadedFile

from ..fixtures import paths
from ... import forms


def test_upload_no_file():
    form = forms.UploadForm()
    assert not form.is_valid()


def test_upload_invalid_sqlite_database_file():
    uploaded_file = SimpleUploadedFile("database", b"data")
    form = forms.UploadForm(files={"database": uploaded_file})
    assert not form.is_valid()


def test_upload_valid_sqlite_database_file():
    with open(paths.database, "rb") as database_file:
        uploaded_file = SimpleUploadedFile("database", database_file.read())
        form = forms.UploadForm(files={"database": uploaded_file})
        assert form.is_valid()
