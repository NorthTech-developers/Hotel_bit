from django import forms
from .models import Habitacion, Reserva_habitacion

class ReservaHabitacion(forms.ModelForm):

    class Meta:
        model = Habitacion
        fields = ('nombre', 'cantidad_habitaciones', 'precio', 'capacidad', 'disponible')



class Crear_Reserva(forms.ModelForm):

    class Meta:
        model = Reserva_habitacion
        fields = ('Nombre_usuario', 'Numero_Personas', 'Fecha_ingreso', 'Fecha_egreso', 'Nombre_habitacion')

