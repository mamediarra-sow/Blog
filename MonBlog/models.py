from djongo import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models.
    
class Author(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    def _str__(self):
        return self.username           
class Publication(models.Model):
    categories=()
    titre=models.CharField(max_length=255)
    categorie=models.CharField(max_length=255,choices=categories)
    description=models.TextField()
    media=models.FileField(upload_to='')
    like=models.IntegerField()
    
    def __strs__(self):
        return self.titre
            
class Commentaire(models.Model):
    utlisateur=models.EmbeddedField(model_container=Author)
    publication=models.EmbeddedField(model_container=Publication)
    comment=models.TextField()
    


