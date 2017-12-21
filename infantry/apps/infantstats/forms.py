from django import forms


class Sqlite3DatabaseFileField(forms.FileField):
    def validate(self, value):
        super().validate(value)
        header = value.readline()
        if not header.startswith(b"SQLite format 3"):
            raise forms.ValidationError("This is not a sqlite3 database file")


class UploadForm(forms.Form):
    database = Sqlite3DatabaseFileField()
