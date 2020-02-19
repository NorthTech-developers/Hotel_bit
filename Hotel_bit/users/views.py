from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse
from .forms import RegisterForm


def welcome(request):
    # para volver al inicio en caso de logeo correcto
    if request.user.is_authenticated:
        return redirect('')
    # vuelve al login en cualquier otro caso
    return redirect('/login')


def registro(request):
    template = "registro.html"

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = RegisterForm

    context = {
    'form': form,
    }
    return render (request, template, context)


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            
            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "users/login.html", {'form': form})


def logout(request):
    do_logout(request)
    return redirect('/')
