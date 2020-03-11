from djongo import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models.
    
class Author(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    def _str__(self):
        return self.username           
class Publication(models.Model):
    categories=(
        ('Makeup steps','Makeup steps'),
        ('Makeup peau noire','Makeup peau noire'),
        ('Makeup peau claire','Makeup peau claire'),
        ('Makeup soft','Makeup soft'),
        ('Makeup fantaisie','Makeup fantaisie'),
        ('Consils beauté','Consils beauté')
    )
    titre=models.CharField(max_length=255)
    categorie=models.CharField(max_length=255,choices=categories)
    description=models.TextField()
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    media=models.FileField(upload_to='')
    like=models.IntegerField(default='null')
    
    def __strs__(self):
        return self.titre
            
class Commentaire(models.Model):
    utlisateur=models.EmbeddedField(model_container=Author)
    publication=models.EmbeddedField(model_container=Publication)
    comment=models.TextField()
class Like(models.Model):
    utlisateur=models.EmbeddedField(model_container=Author)
    publication=models.EmbeddedField(model_container=Publication)
    on_click=models.BooleanField(default=False)
    
    


