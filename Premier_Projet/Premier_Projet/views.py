# Dans votre_app/views.py
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello")
