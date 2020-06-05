from datetime import datetime

from mongoengine import *
from django.db import models

# Create your models here.
connect(
    db='myapp1',
    host='mongodb+srv://gauravjana:justimagine@cluster0-ge8xe.mongodb.net/myapp1?retryWrites=true&w=majority',
    username='gauravjana',
    password='justimagine',
)


class Register(Document):
    username = StringField(max_length=50, required=True)
    email = StringField(max_length=50, required=True)
    password = StringField(required=True)

    def __str__(self):
        return self.username