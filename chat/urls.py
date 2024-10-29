from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submitMessage", views.submitMessage, name="submitMessage"),
]
