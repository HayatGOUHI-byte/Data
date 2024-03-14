from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse




def index(request):
	return HttpResponse("hey there")
	



def reconna(request):
	return HttpRequest("django pages here")

def search(request):
	if request.method == "POST":
		return HttpResponse("C est une methode post {}".format(request.method))
	else:
		return HttpResponse("c est une methode get {}".format(request.method))


