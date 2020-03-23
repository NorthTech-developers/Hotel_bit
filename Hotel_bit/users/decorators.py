#Esto es para restringir que un usuario comun pueda acceder a ciertas paginas 

from django.http import HttpResponse
from django.shortcuts import redirect

#si el usuario esta logeado no lo deja acceder
def usuariologeado(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func