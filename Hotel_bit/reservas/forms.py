from django import forms
from .models import Habitacion, Reserva_habitacion
from .models import Habitaciones, Reserva, Tipo_alojamiento, Tipo_pension, Precio_pension, Reservas_habitacion, CantidadReservas

class CantidadReservasForm(forms.ModelForm):
	class Meta:
		model : CantidadReservas
		fields = '__all__'


class HabitacionForm(forms.ModelForm):
	class Meta:
		model : Habitaciones
		fields = 'cantidad',

class ReservaForm(forms.ModelForm):
	class Meta:
		model = Reserva
		fields = '__all__'
		widgets = {
            'fecha_reserva': forms.widgets.SelectDateWidget(years=range(2019, 2021))
        }

class Actualizacion(forms.ModelForm):
	class Meta:
		model = Reservas_habitacion
		fields = 'status_payment', 'metodo_de_pago'


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
		fields = 'id', 'usuario', 'fecha_entrada', 'fecha_salida', 'ocupantes', 'reserva_habitacion', 'precio_total', 'identificador', 'metodo_de_pago','status_payment'
		widgets = {
            'fecha_entrada': forms.widgets.SelectDateWidget(years=range(2019, 2021)),
            'fecha_salida': forms.widgets.SelectDateWidget(years=range(2019, 2021)),
        }
		fecha_entrada = 'fecha_entrada'
		fecha_salida = 'fecha_salida'
		if fecha_entrada > fecha_salida:
			raise forms.ValidationError("Fecha de salida debe ser mayor a la fecha de entrada")

class Actualizar_Reserva_Habitacion (forms.ModelForm):
	
	class Meta:
		model = Reservas_habitacion
		fields = ('metodo_de_pago', 'status_payment')


class ReservaHabitacion(forms.ModelForm):

    class Meta:
        model = Habitacion
        fields = ('nombre', 'cantidad_habitaciones', 'precio', 'capacidad', 'disponible')



class Crear_Reserva(forms.ModelForm):

    class Meta:
        model = Reserva_habitacion
        fields = ('Nombre_usuario', 'Numero_Personas', 'Fecha_ingreso', 'Fecha_egreso', 'Nombre_habitacion')

