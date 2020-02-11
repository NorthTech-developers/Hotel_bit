from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import ReservaHabitacion


# Create your views here.

def reservar(request):
    return render(request, 'reservar.html', {})

def reserva(request):
    form = ReservaHabitacion()
    return render(request, 'editar_reserva.html', {'form':form})


