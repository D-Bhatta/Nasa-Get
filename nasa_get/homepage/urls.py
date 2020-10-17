from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("addkey/", views.homepage, name="homepage"),
]
