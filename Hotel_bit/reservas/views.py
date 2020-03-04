from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import ReservaHabitacion, Crear_Reserva
from .models import Habitacion, Reserva_habitacion, Habitaciones
from datetime import date, datetime
from _datetime import timedelta


# Create your views here.

def reservar(request):
    
    return render(request, 'reservar.html', {})

def editar_reserva(request): 

    a = datetime.now()
    hoy = int(a.strftime('%d%m%Y'))
    habitacion = Habitaciones.objects.all()
    reserva = Reserva_habitacion.objects.all()

    if request.POST.get('Numero_Personas'):
        numero_personas = int(request.POST.get('Numero_Personas'))
        habitacion = habitacion.filter(capacidad__gt=numero_personas)
        
        fecha_egreso_sucia = request.POST.get('Fecha_egreso')
        fecha_egreso_limpia = str(fecha_egreso_sucia).replace('-', '') # sustituimos el simbolo - por nada quedando un str de numeros
        fecha_egreso = datetime.strptime(fecha_egreso_sucia, '%Y-%m-%d') #Transformación del string a tipo Date Objects

        fecha_ingreso_sucia = request.POST.get('Fecha_ingreso')
        fecha_ingreso_limpia = str(fecha_ingreso_sucia).replace('-', '') # sustituimos el simbolo - por nada quedando un str de numeros
        fecha_ingreso = datetime.strptime(fecha_ingreso_sucia, '%Y-%m-%d') #Transformación del string a tipo Date Objects
        
        dias_reserva = fecha_egreso - fecha_ingreso
    else:
        dias_reserva = "Completar Formulario"

       
    return render(request, 'editar_reserva.html', {'habitacion':habitacion, 'dias_reserva': dias_reserva, 'fecha_ingreso': fecha_ingreso, 'fecha_egreso': fecha_egreso })

