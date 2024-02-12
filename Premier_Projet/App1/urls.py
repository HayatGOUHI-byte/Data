from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
path("index/", views.index, name="index"),
path("Commande/", views.Commande, name="Commande"),
path("Produit/", views.Produit, name="Produit"),
path("Client/", views.Client, name="Client")
]

