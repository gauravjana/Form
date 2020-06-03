'''
from __future__ import unicode_literals


from django.db import models
'''
from mongoengine import *
from mongoengine import Document,fields
from datetime import datetime
import os
import json

connect(
    db='myapp1',
    host='mongodb+srv://gauravjana:justimagine@cluster0-ge8xe.mongodb.net/myapp1?retryWrites=true&w=majority',
    username='gauravjana',
    password='justimagine',
)


'''
class Document(models.Model):
    COMPANY_NAME = models.CharField(max_length=255, blank=True)
    FRONT_INSIDE_PICTURE= models.FileField(upload_to='documents/')
    BUSINESS_CARD_IMAGE = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
'''
class data(Document):


    COMPANY_NAME = StringField(max_length=255, required=True)
    FRONT_INSIDE_PICTURE = FileField()
    BUSINESS_CARD_IMAGE = FileField()
    uploaded_at = DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.name






