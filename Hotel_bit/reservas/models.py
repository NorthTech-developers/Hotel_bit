from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

precio_pension = (
	(150.00, 150.00),
	(100.00, 100.00),
	(60.00, 60.00),
	(0.00, 0.00)
)

pension = (
	('completa', 'completa'),
	('media', 'media'),
	('desayuno', 'desayuno'),
	('nada', 'nada')
)

tipo_alojamiento = (
	('doble', 'doble'),
	('individual', 'individual')
)

precio_alojamiento = (
	(200, 200),
	(100, 100),
	(300, 300),
	(400, 400),
	(500, 500),
	(600, 600),
	(700, 700),
	(800, 800),
	(900, 900),
	(1000, 1000)
)

tipo_de_pago = (

	('Mercado Pago', 'Mercado Pago'),
	('Efectivo', 'Efectivo'),
	('Pendiente', 'Pendiente')

)

status_payment = (

	('Aprovado', 'Aprovado'),
	('Pendiente', 'Pendiente'),
	('Fallo', 'Fallo'),
	('Cancelado', 'Cancelado'),
	('Activa', 'Activa'),
	('Finalizada', 'Finalizada')
			
)


class Tipo_pension(models.Model):
	tipo_pension = models.CharField(choices=pension, max_length=50)

	def __str__(self):
		return self.tipo_pension

	class Meta:
		verbose_name = 'Tipo Pension'
		verbose_name_plural = 'Tipo Pensiones'

class Precio_pension(models.Model):
	precio = models.DecimalField(choices=precio_pension, max_digits=5, decimal_places=2)
	precio_tipo_pension = models.ForeignKey('Tipo_pension', on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.precio_tipo_pension)

	class Meta:
		verbose_name = 'Precio Pension'
		verbose_name_plural = 'Precio Pensiones'

class Habitaciones(models.Model):
	descripcion = models.CharField(max_length=150)
	image = models.ImageField(upload_to='habitaciones/')
	num_habitacion = models.IntegerField(default=0)
	baños = models.IntegerField(default=0)
	garaje = models.IntegerField(default=0)
	camas = models.IntegerField(default=0)
	capacidad = models.IntegerField(default=1)
	cantidad = models.IntegerField(default=1)
	
	def __str__(self):
		return self.descripcion

	class Meta:
		verbose_name = 'Habitacion'
		verbose_name_plural = 'Habitaciones'

class Tipo_alojamiento(models.Model):
	descripcion = models.CharField(choices=tipo_alojamiento, max_length=50)
	precio = models.DecimalField(choices=precio_alojamiento, max_digits=5, decimal_places=2)
	habitacion_tipo_alojamiento = models.ForeignKey('Habitaciones', on_delete=models.CASCADE)

	def __str__(self):
		return self.descripcion

	class Meta:
		verbose_name = 'Tipo Alojamiento'
		verbose_name_plural = 'Tipos Alojamientos'

class Reserva(models.Model):
	reserva = models.ForeignKey(User, on_delete=models.CASCADE)
	fecha_reserva = models.DateField(default=datetime.date.today)

	def __str__(self):
		return str(self.fecha_reserva)

	class Meta:
		verbose_name = 'Reserva'
		verbose_name_plural = 'Reservas'

class Valoraciones(models.Model):
	fecha = models.DateField()
	valoracion = models.IntegerField(default=0)
	valoracion_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	valoracion_reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE)

	def __str__(self):
		return self.valoracion_usuario

	class Meta:
		verbose_name = 'Valoración'
		verbose_name_plural = 'Valoraciones'


class Reservas_habitacion(models.Model):
	fecha_entrada = models.DateField()
	fecha_salida = models.DateField()
	ocupantes = models.IntegerField(default=0)
	reserva_habitacion = models.ForeignKey('Habitaciones', on_delete=models.CASCADE)
	reserva_reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE)
	precio_total = models.IntegerField('precio_total', default=0)
	identificador = models.IntegerField('identificador', blank=False, null=False, default=12341234)
	metodo_de_pago = models.CharField(choices=tipo_de_pago, max_length=100,default='Pendiente')
	status_payment = models.CharField(choices=status_payment, max_length=100, default='Pendiente')
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.reserva_habitacion)

	class Meta:
		verbose_name = 'Reserva habitacion'
		verbose_name_plural = 'Reservas habitaciones'


class CantidadReservas(models.Model):
	reserva_habitacion = models.ForeignKey('Habitaciones', on_delete=models.CASCADE)
	limite = models.IntegerField('limite', default=10)

	class Meta:
		verbose_name = 'Cantidad de Reservas'
		verbose_name_plural = 'Cantidad de Reservas'

	def __str__(self):
		return str(self.reserva_habitacion)
	

# Los modelos de arriba los agregue hoy


class Habitacion(models.Model):
    nombre = models.CharField("nombre habitacion", max_length=50)
    cantidad_habitaciones = models.IntegerField('cantida de habitaciones', default=10)
    precio = models.IntegerField("precio habitacion")
    capacidad = models.IntegerField("capacidad de usuarios")
    disponible = models.BooleanField("esta disponible", default=True)
    
  
    def __str__(self):
        return self.nombre
    
class Reserva_habitacion(models.Model):
    Nombre_usuario = models.CharField("Nombre usuario" , max_length=200, blank=False, null=False)
    Numero_Personas = models.IntegerField("Cantidad de Personas", blank=False, null=False)
    Fecha_ingreso = models.CharField("fecha_ingreso", max_length=20, blank=False, null=False)
    Fecha_egreso = models.CharField("fecha_egreso", max_length=20, blank=False, null=False)
    Nombre_habitacion = models.CharField("nombre habitacion", max_length=100, blank=False, null=False, default='Simple room')  

    def __str__(self):
        return self.Nombre_usuario
    
    
