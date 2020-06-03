from rest_framework_mongoengine import serializers
from .models import data


class dataserializer(serializers.DocumentSerializer):
    class Meta:
        model = data
        fields = "__all__"
