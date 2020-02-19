from django import forms
from .models import RegistroUsuario

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
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
            'password',
            'password2',
            'terminos_condiciones',
            'email_newsletter',
            )