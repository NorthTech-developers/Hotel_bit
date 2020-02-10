from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservar, name="reservar"),

]
