from dataclasses import field
from django import forms
from .models import DemoUrl

class UrlForm(forms.ModelForm):
    class Meta:
        model = DemoUrl
        fields = ['long_url']