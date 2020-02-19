from django.shortcuts import render
from newsletters.forms import NewsletterForm
from newsletters.views import Newsletter

# Create your views here.

def home(request):
    template = "index.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})


def habitaciones(request):
    template = "room.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})


def galeria(request):
    template = "galeria.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})


def sobre_nosotros(request):
    template = "about.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})


def habitacion_vip(request):
    template = "single-room.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})


def login(request):
    template = "login.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})


def registro(request):
    template = "registro.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})

