from django import forms
from .models import Comentario

class DejarUnComentario(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('autor', 'texto')
