'''
from __future__ import unicode_literals

class Document(models.Model):
    COMPANY_NAME = models.CharField(max_length=255, blank=True)
    FRONT_INSIDE_PICTURE= models.FileField(upload_to='documents/')
    BUSINESS_CARD_IMAGE = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


from django.db import models
'''
import json
from datetime import datetime

from mongoengine import *

connect(
    db='myapp1',
    host='mongodb+srv://gauravjana:justimagine@cluster0-ge8xe.mongodb.net/myapp1?retryWrites=true&w=majority',
    username='gauravjana',
    password='justimagine',
)




class Content(Document):
    COMPANY_NAME = StringField(max_length=255, required=True)
    email = StringField(max_length=255, required=True)
    address = StringField(max_length=455, blank=True)
    FRONT_INSIDE_PICTURE = FileField()
    BUSINESS_CARD_IMAGE = FileField()
    uploaded_at = DateTimeField(default=datetime.utcnow)




class Login(Document):
    username = StringField(max_length=50, required=True)
    email = StringField(max_length=50, required=True)
    password = StringField(required=True)

    def __str__(self):
        return self.username
