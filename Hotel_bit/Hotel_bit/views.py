from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def habitaciones(request):
    return render(request, 'room.html', {})

def galeria(request):
    return render(request, 'galeria.html', {}) 

def sobre_nosotros(request):
    return render(request, 'about.html', {})

def habitacion_vip(request):
    return render(request, 'single-room.html', {})

def login(request):
    return render(request, 'login.html', {})

