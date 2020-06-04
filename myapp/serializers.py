from rest_framework_mongoengine import serializers

from django.contrib.auth.models import User
from .models import data


class dataserializer(serializers.DocumentSerializer):
    class Meta:
        model = data
        fields = ('COMPANY_NAME', 'email', 'address','FRONT_INSIDE_PICTURE','BUSINESS_CARD_IMAGE')



