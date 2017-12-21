from django.urls import path

from infantry.apps.infantstats import views

base_url = "statistics-base-url"
upload_url = "statistics-upload-url"

urlpatterns = [
    path("", views.basic_stats, name=base_url),
    path("upload", views.upload, name=upload_url)
]
