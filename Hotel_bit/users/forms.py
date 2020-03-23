from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField

class CustomUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 
        'last_name', 
        'email', 
        'username', 
        'password1', 
        'password2',
        )
