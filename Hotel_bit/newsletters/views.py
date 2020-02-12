from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import NewsletterForm
# Create your views here.

def contacto(request):
    template = "base.html"

    if request.method == "POST":
        form = NewsletterForm.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = NewsletterForm

    context = {
    'form': form,
    }
    return render (request, template, context)