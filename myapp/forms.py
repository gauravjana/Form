from django import forms
from mongodbforms import DocumentForm

from .models import Content


class ContactForm(DocumentForm):
    class Meta:
        document = Content
        fields = ('COMPANY_NAME', 'email', 'address', 'FRONT_INSIDE_PICTURE', 'BUSINESS_CARD_IMAGE')

