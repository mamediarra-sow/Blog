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
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/blog-single.html',locals())

def BlogPage(request):
    posts=Publication.objects.all()
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
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
def Steps(request):
    categories=Publication.objects.filter(categorie="Makeup steps")
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/steps.html',locals())

def BlackSkin(request):
    categories=Publication.objects.filter(categorie="Makeup peau noire")
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/black.html',locals())

def WhiteSkin(request):
    categories=Publication.objects.filter(categorie="Makeup peau claire")
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/white.html',locals())

def Soft(request):
    categories=Publication.objects.filter(categorie="Makeup soft")
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/soft.html',locals())

def Soiree(request):
    categories=Publication.objects.filter(categorie="Makeup soirée")
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/soiree.html',locals())

def Conseils(request):
    categories=Publication.objects.filter(categorie="Conseils beauté")
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/conseil.html',locals())