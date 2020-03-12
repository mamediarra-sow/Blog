from .models import *
from django import forms

class AuthorForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())