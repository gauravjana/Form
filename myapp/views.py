'''

from django.shortcuts import render, redirect
from .forms import ContactForm
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
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from .forms import ContactForm
from .models import Content
from .serializers import dataserializer


def home(request):

    return render(request, 'home.html')
    # documents = Document.objects.all()
    # return render(request, 'home.html', { 'documents': documents })




@login_required()
def model_form_upload(request):
    if request.method == 'POST':
        frm = ContactForm(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('home')
    else:
        frm = ContactForm()
    return render(request, 'model_form_upload.html', {
        'form': frm
    })

class DataView(APIView):

    def get(self, request):
        list = Content.objects.all()
        serializer = dataserializer(list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = dataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
