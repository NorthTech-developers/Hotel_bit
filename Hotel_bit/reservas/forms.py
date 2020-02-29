from django import forms
from .models import Habitacion, Reserva_habitacion
from .models import Hotel, Habitaciones, Reserva, Tipo_alojamiento, Tipo_pension, Precio_pension, Reservas_habitacion

class ReservaForm(forms.ModelForm):
	class Meta:
		model = Reserva
		fields = '__all__'
		widgets = {
            'fecha_reserva': forms.widgets.SelectDateWidget(years=range(2019, 2021))
        }

class TipoAlojamientoForm(forms.ModelForm):
	class Meta:
		model = Tipo_alojamiento
		fields = '__all__'

class TipoPensionForm(forms.ModelForm):
	class Meta:
		model = Tipo_pension
		fields = '__all__'

class PrecioPensionForm(forms.ModelForm):
	class Meta:
		model = Precio_pension
		fields = '__all__'

class ReservasHabitacionForm(forms.ModelForm):
	class Meta:
		model = Reservas_habitacion
		fields = 'id', 'fecha_entrada', 'fecha_salida', 'ocupantes', 'reserva_habitacion'
		widgets = {
            'fecha_entrada': forms.widgets.SelectDateWidget(years=range(2019, 2021)),
            'fecha_salida': forms.widgets.SelectDateWidget(years=range(2019, 2021)),
        }
		fecha_entrada = 'fecha_entrada'
		fecha_salida = 'fecha_salida'
		if fecha_entrada > fecha_salida:
			raise forms.ValidationError("Fecha de salida debe ser mayor a la fecha de entrada")


class ReservaHabitacion(forms.ModelForm):

    class Meta:
        model = Habitacion
        fields = ('nombre', 'cantidad_habitaciones', 'precio', 'capacidad', 'disponible')



class Crear_Reserva(forms.ModelForm):

    class Meta:
        model = Reserva_habitacion
        fields = ('Nombre_usuario', 'Numero_Personas', 'Fecha_ingreso', 'Fecha_egreso', 'Nombre_habitacion')

