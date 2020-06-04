from rest_framework_mongoengine import serializers

from django.contrib.auth.models import User
from .models import Content, Login


class dataserializer(serializers.DocumentSerializer):
    class Meta:
        model = Content
        fields = ('COMPANY_NAME', 'email', 'address', 'FRONT_INSIDE_PICTURE', 'BUSINESS_CARD_IMAGE')


class Register(serializers.DocumentSerializer):
    class Meta:
        model = Login
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class login(serializers.DocumentSerializer):
    class Meta:
        model = Login
        fields = ('username','password')
        extra_kwargs = {'password': {'write_only': True}}