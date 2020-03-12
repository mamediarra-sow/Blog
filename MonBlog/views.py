from django.shortcuts import render
from .models import *

# Create your views here.
def HomePage(request):
    return render(request,'Blog/index.html')

def AboutPage(request):
    return render(request,'Blog/about.html')

def SingleBlogPage(request,id):
    post=Publication.objects.get(id=id)
    return render(request,'Blog/blog-single.html',locals())

def BlogPage(request):
    posts=Publication.objects.all()
    return render(request,'Blog/blog.html',locals())

def ContactPage(request):
    return render(request,'Blog/contact.html')


