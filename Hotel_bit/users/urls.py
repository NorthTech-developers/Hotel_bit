from django.urls import path
from . import views

urlpatterns = [
    #path('', views.welcome, name="welcome"),
    path('registro', views.registro, name="registro"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('ver_perfil', views.ver_perfil, name="ver_perfil")
]
