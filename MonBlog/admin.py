from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Publication)
admin.site.register(Author)
admin.site.register(Commentaire)