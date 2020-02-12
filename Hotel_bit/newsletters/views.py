from django.shortcuts import render
from .forms import NewsletterForm
# Create your views here.

def NewsletterUser(request):
    template = "base.html"

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