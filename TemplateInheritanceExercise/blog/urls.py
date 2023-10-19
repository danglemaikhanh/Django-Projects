from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="homepage"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
]
