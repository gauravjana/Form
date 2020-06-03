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
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from .models import data
from .serializers import dataserializer

class DataView(viewsets.ModelViewSet):

    lookup_field = 'id'
    serializer_class = dataserializer

    def get_queryset(self):
        return data.objects.all()

    def post(self, request):
        serializer = dataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
