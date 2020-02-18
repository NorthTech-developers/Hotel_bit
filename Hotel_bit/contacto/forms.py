from django import forms
from .models import contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ('first_name',  'last_name',  'phone',  'email',  'message')