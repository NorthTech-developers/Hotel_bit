from django.shortcuts import render

# Create your views here.

def reservar(request):
    return render(request, 'reservar.html', {})