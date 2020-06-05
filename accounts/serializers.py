from rest_framework_mongoengine import serializers


from django.contrib.auth.models import User
from .models import Register


# class Register(serializers.DocumentSerializer):
#     class Meta:
#         model = Login
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#
# class login(serializers.DocumentSerializer):
#     class Meta:
#         model = Login
#         fields = ('username','password')
#         extra_kwargs = {'password': {'write_only': True}}


class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Register
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True,'required':True}}
    # def create(self, validated_data):
    #     user = User.objects.create(**validated_data)
    #     return user