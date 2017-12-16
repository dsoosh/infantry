from django.urls import path

from infantry.apps.infantstats import views

base_url = "statistics-base-url"

urlpatterns = [
    path("", views.basic_stats, name=base_url)
]
