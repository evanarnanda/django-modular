from django.urls import path

from . import views

urlpatterns = [
    path("", views.user_settings, name="user settings"),
]