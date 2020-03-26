from django.urls import path
from . import views

urlpatterns = [
    # path('', views.reservar, name="reservar"),
    path('editar_reserva', views.editar_reserva, name="editar_reserva",),
    path('habitacion_datail', views.habitacion_detail, name="habitacion_detail"),
    path('confirmar_pago', views.confirmar_pago, name="confirmar_pago"),
    path('mercado_pago', views.mercado_pago, name="mercado_pago"),
    path('actualizacion',views.actualizacion, name="actualizacion"),
    

]
