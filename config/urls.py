"""URL configuration for the django-api starter."""
from django.urls import path

from api import views

urlpatterns = [
    path("", views.index, name="index"),
    path("health", views.health, name="health"),
    path("api/hello", views.hello, name="hello"),
]
