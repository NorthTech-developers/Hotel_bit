from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservar, name="reservar"),
    path('editar_reserva', views.editar_reserva, name="editar_reserva",)

]
