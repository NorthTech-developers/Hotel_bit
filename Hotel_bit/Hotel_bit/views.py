from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def habitaciones(request):
    return render(request, 'room.html', {})

def galeria(request):
    return render(request, 'index.html', {}) 

def sobre_nosotros(request):
    return render(request, 'about.html', {})