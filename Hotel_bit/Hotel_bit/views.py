from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from reservas.models import Habitacion

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def habitaciones(request):
    habitacion = Habitacion.objects.all()
    return render(request, 'room.html', {'habitacion': habitacion})

def galeria(request):
    return render(request, 'galeria.html', {}) 

def sobre_nosotros(request):
    return render(request, 'about.html', {})

def habitacion_vip(request):
    return render(request, 'single-room.html', {})

def login(request):
    return render(request, 'login.html', {})

def registro(request):
    return render(request, 'registro.html', {})

def logout(request):
    do_logout(request)
    return redirect('/')


