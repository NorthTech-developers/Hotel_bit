from django import forms
from .models import Habitacion

class ReservaHabitacion(forms.ModelForm):

    class Meta:
        model = Habitacion
        fields = ('nombre', 'cantidad_habitaciones', 'precio', 'capacidad', 'disponible')