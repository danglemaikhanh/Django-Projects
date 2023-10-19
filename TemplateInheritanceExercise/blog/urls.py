from django.urls import path
from . import views

urlpatterns = [
    # redirects to views.home
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
]
