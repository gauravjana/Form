from django import forms
from .models import Document


class ContactForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = "__all__"

