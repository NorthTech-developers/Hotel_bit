from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import CustomUserForm
from .decorators import usuariologeado

@usuariologeado
def registro(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            #Los usuarios registrados quedan en el grupo usuariocomun
            group = Group.objects.get(name='dc')
            user.groups.add(group)
            Profile.objects.create(
                user=user
            )




            messages.success(request, 'Cuenta creada con exito')

            return redirect('login')
    context = {'form':form}
    return render(request, 'registro.html', context)

@usuariologeado
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            do_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Usuario y/o contrase;a incorrectos')

    context = {}
    return render(request, "login.html", context)


def logout(request):
    do_logout(request)
    return redirect('/')

@login_required(login_url='login')
def ver_perfil(request):
    return render(request, 'perfil.html') 