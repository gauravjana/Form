from django.shortcuts import render
from django.http import HttpResponse
from .forms import  ContactForm


# Create your views here.

def model_form_upload(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })