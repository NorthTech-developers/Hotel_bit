from .forms import NewsletterForm


def Newsletter(request):    
    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = NewsletterForm


