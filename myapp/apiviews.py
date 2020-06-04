from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Login
from .serializers import login, Register
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class LoginView(APIView):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    #permission_classes = (IsAuthenticated,)

    lookup_field = 'id'
    serializer_class = login

    def post(self, request):
        groups = Login.objects.all()
        data = request.data
        serializer = login(data=request.data)
        if serializer.is_valid():
            for group in groups:
                if data['password'] == group['password'] and data['username'] == group['username']:
                    return Response(status=status.HTTP_200_OK)
                else :
                    return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Registration(APIView):

    lookup_field = 'id'
    serializer_class = Register

    def get_queryset(self):
        return Login.objects.all()

    def post(self, request):
        serializer = Register(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

