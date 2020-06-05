from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.response import Response

from accounts.serializers import UserSerializer
from .models import Register




def logout_user(request):
    logout(request)
    return redirect('/')


def login_form(request):
    return render(request, 'accounts/login.html', {})


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            login(request, user)
            return redirect('/data')
    return redirect(settings.LOGIN_URL, request)

class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Register.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def post(self, request):
        serializer = Register(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Create your views here.
