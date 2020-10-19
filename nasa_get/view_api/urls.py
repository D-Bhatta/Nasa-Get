from django.urls import path

from . import views

urlpatterns = [
    path("", views.api_index, name="apis"),
    path("<int:id>/", views.api_result, name="api_result"),
]
