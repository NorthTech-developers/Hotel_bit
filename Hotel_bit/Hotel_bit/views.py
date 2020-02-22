from django.shortcuts import render, redirect
from newsletters.forms import NewsletterForm
from users.forms import RegisterForm, Autenticacion
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    template = "index.html"

    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = NewsletterForm

    context = {
    'form': form,
    }
    return render (request, template, context)


def habitaciones(request):
    template = "habitaciones.html"

    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = NewsletterForm

    context = {
    'form': form,
    }
    return render (request, template, context)


def galeria(request):
    template = "galeria.html"

    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = NewsletterForm

    context = {
    'form': form,
    }
    return render (request, template, context)


def sobre_nosotros(request):
    template = "about.html"

    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = NewsletterForm

    context = {
    'form': form,
    }
    return render (request, template, context)


def habitacion_vip(request):
    template = "sigle-room.html"

    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = NewsletterForm

    context = {
    'form': form,
    }
    return render (request, template, context)


def registro(request):
    template = "registro.html"

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            if user is not None:
                do_login(request, user)
                return redirect('/')
    
    else:
        form = RegisterForm

    context = {
    'form': form,
    }
    return render (request, template, context)


def login(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = Autenticacion(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user:
				do_login(request, user)
				return redirect("home")

	else:
		form = Autenticacion()

	context['login_form'] = form

	# print(form)
	return render(request, "users/login.html", context)

