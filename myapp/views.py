from django.shortcuts import render,redirect
from .forms import  ContactForm
from .models import Document



# Create your views here.
def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })

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