from djongo import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models.
    
class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
             
class Publication(models.Model):
    categories=(
        ('Makeup steps','Makeup steps'),
        ('Makeup peau noire','Makeup peau noire'),
        ('Makeup peau claire','Makeup peau claire'),
        ('Makeup soft','Makeup soft'),
        ('Makeup fantaisie','Makeup fantaisie'),
        ('Conseils beauté','Conseils beauté')
    )
    titre=models.CharField(max_length=255)
    categorie=models.CharField(max_length=255,choices=categories)
    description=models.TextField()
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    media=models.FileField(upload_to='')
    like=models.IntegerField(default="null")
    
    
            
class Commentaire(models.Model):
    auteur=models.CharField(max_length=255)
    publication=models.EmbeddedField(model_container=Publication)
    comment=models.TextField()
class Like(models.Model):
    auteur=models.CharField(max_length=255)
    publication=models.EmbeddedField(model_container=Publication)
    
    


