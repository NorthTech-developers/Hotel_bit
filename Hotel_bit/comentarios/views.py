from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Comentario
from .forms import ComentarioForm


# Create your views here.

def comments(request):
    user_comments = Comentario.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'comentarios/comments.html', {'user_comments': user_comments})

@login_required
def user_comments(request):
    if request.method == "POST":
        form = ComentarioForm
    form = ComentarioForm(request.POST)
    if form.is_valid():
        comentarios = form.save(commit=False)
        comentarios.autor = request.user
        comentarios.save()
        return redirect('comments')
    else:
        form = ComentarioForm
    return render(request, 'comentarios/user_comments.html', {'form': form})