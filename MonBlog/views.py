from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib.auth.models import update_last_login

# Create your views here.
def HomePage(request):
    return render(request,'Blog/index.html')

def AboutPage(request):
    return render(request,'Blog/about.html')

def SingleBlogPage(request,id):
    post=Publication.objects.get(id=id)
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    return render(request,'Blog/blog-single.html',locals())

def BlogPage(request):
    posts=Publication.objects.all()
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    return render(request,'Blog/blog.html',locals())

def ContactPage(request):
    return render(request,'Blog/contact.html')
def Login(request):
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('HomePage')
    form=AuthorForm()
    return render(request,'Blog/login.html',locals())
def LikePost(request,id):
    post=Publication.objects.get(id=id)
    try:
        like=Like.objects.get(auteur=request.user.username, publication=post)
    except Like.DoesNotExist:
        post.like+=1
        post.save()
        new_like = Like.objects.create(auteur=request.user.username, publication=post)
        return redirect('SingleBlogPage' , id)
    return render(request,'Blog/blog-single.html',locals())
#def Categorie(request):
   # posts=request.post.all()
    #for post in posts:
       # if post.categorie=="Makeup steps":
           # return render (request,'Blog/step.html',locals())
    #return render (request,'Blog/step.html',locals())
