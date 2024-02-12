from django.shortcuts import render
from django.http import HttpResponse



def index(request):
	return HttpResponse("hello my cousin")

# Create your views here.


def Commande(request):
	return HttpResponse("this page is for Commande")


def Client(request):
	return HttpResponse("this page is for Client")


def Produit(request):
	return HttpResponse("this page is for Produit")
