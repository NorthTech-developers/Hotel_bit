from django.db import models


class Habitacion(models.Model):
    nombre = models.CharField("nombre habitacion", max_length=50)
    cantidad_habitaciones = models.IntegerField('cantida de habitaciones', default=1)
    precio = models.IntegerField("precio habitacion")
    capacidad = models.IntegerField("capacidad de usuarios")
    disponible = models.BooleanField("esta disponible", default=True)
    
  
    def __str__(self):
        return self.nombre
    
