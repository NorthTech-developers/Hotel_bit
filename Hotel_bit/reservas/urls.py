from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('', views.reservar, name="reservar"),
    path('editar_reserva', views.filtrar, name="editar_reserva",),
    path('habitacion_datail', login_required(views.habitacion_detail), name="habitacion_detail"),
    # path('confirmar_pago', views.confirmar_pago, name="confirmar_pago"),
    path('mercado_pago', views.mercado_pago, name="mercado_pago"),
    path('actualizacion',views.actualizacion, name="actualizacion"),
    path('cancel_res', views.cancel_res, name="cancel_res"),
    path('mis_reservas', views.listar_reservas, name="mis_reservas"),
    path('eliminar_reserva', views.eliminar_reserva, name="eliminar_reserva"),
    

]
