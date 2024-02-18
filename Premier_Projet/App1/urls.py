from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
path("index/", views.index, name="index"),
path("clients/", views.list_clients, name="list_clients"),
path("client/<int:client_id>/", views.client_detail, name="client_detail"),
path("client/create", views.create_client, name="create_client"),
path("client/<int:client_id>/update/", views.update_client, name="update_client"),
path("client/<int:client_id>/delete/", views.delete_client, name="delete_client"),
path("voiture/",views.all_voiture, name="all_voiture"),
path("create_voiture/",views.create_voiture, name="create")
]

