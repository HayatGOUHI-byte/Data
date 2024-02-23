from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Client
from .models import Voiture
from django import forms
from django.forms import ModelForm



def index(request):
	return HttpResponse("welcome back")


#afficher tous les clients de la base de données
def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


#afficher les détails d'un client spécifique
def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client_detail.html', {'client': client})


#créer un nouveau client

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})


#mettre à jour des détails d'un client


def create_voiture(request):
    if request.method == "POST":
        form = VoitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_voiture')
    else:
        form = VoitureForm()
    return render(request, 'create_voiture.html', {'form': form})

def update_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form})



  #supprimer un client

def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('list_clients')
    return render(request, 'delete_client_confirmation.html', {'client': client})





def all_voiture(request):
    voitures = Voiture.objects.all()
    return render(request,'all_voitures.html', {'voitures': voitures})


def delete_voiture(request):
        return HttpResponse("hello")



def all_Data(request):
    voitures = Voiture.objects.all()
    return render(request,'all_Data.html', {'voitures': voitures})


def all_Data(request):
    voitures = Voiture.objects.all()
    return render(request,'all_Data.html', {'voitures': voitures})

def all_Data(request):
    voitures = Voiture.objects.all()
    return render(request, 'all_Data.html', {'voiture': voitures})