from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
path("index/", views.index, name="index"),
path("search/", views.search, name="search")
]

