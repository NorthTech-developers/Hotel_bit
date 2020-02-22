from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import RegistroUsuario

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = RegistroUsuario
        fields = (
            'first_name',
            'last_name',
            'adress',
            'phone',
            'ci',
            'email',
            'username',
            'password1',
            'password2',
            'terminos_condiciones',
            'email_newsletter',
            )


class Autenticacion(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = RegistroUsuario
		fields = ('username', 'password')

	def clean(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			password = self.cleaned_data['password']
			if not authenticate(username=username, password=password):
				raise forms.ValidationError("Login invalido")