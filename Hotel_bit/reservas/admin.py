from django.contrib import admin
from .models import Habitacion, Reservas_habitacion, Reserva, Habitaciones, Tipo_pension, Precio_pension, Tipo_alojamiento

# Register your models here.

admin.site.register(Habitacion)
admin.site.register(Reservas_habitacion)
admin.site.register(Reserva)
admin.site.register(Habitaciones)
admin.site.register(Tipo_pension)
admin.site.register(Precio_pension)
admin.site.register(Tipo_alojamiento)




   