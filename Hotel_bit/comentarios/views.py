from django.shortcuts import render
from django.utils import timezone
from .models import Comentario

# Create your views here.

def comments(request):
    reviews = Comentario.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'comentarios/comments.html', {'reviews': reviews})