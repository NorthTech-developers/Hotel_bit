from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import ReservaHabitacion
from .models import Habitacion, Reserva_habitacion
from datetime import date, datetime


# Create your views here.

def reservar(request):
    
    return render(request, 'reservar.html', {})

def reserva(request):
    a = datetime.now()
    hoy = int(a.strftime('%d%m%Y'))
    habitacion = Habitacion.objects.all()
    form = ReservaHabitacion()
    reserva = Reserva_habitacion.objects.all() 
    return render(request, 'editar_reserva.html', {'form':form, 'habitacion':habitacion, 'reserva': reserva, 'hoy': hoy})


