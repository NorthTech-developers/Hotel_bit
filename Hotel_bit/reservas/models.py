from django.db import models


class Habitacion(models.Model):
    nombre = models.CharField("nombre habitación", max_length=50)
    cantidad_habitaciones = models.IntegerField('cantidad de habitaciones', default=10)
    precio = models.IntegerField("precio habitación")
    capacidad = models.IntegerField("capacidad de usuarios")
    disponible = models.BooleanField("está disponible", default=True)
    
  
    def __str__(self):
        return self.nombre

    
class Reserva_habitacion(models.Model):
    Nombre_usuario = models.CharField("Nombre usuario" , max_length=200, blank=False, null=False)
    Numero_Personas = models.IntegerField("Cantidad de Personas", blank=False, null=False)
    Fecha_creacion = models.DateTimeField("Fecha de confirmación de la reserva")
    Fecha_ingreso = models.DateField("fecha ingreso", auto_now=False)
    Fecha_egreso = models.DateField("fecha egreso", auto_now=False)
    Nombre_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre_usuario


    
    
