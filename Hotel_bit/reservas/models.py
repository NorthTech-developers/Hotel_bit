from django.db import models


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
    
    
