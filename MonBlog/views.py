from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib.auth.models import update_last_login
from django.core.paginator import Paginator
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
    post_list=Publication.objects.all()
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page',1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
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
########## les j'aimes ###########
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
    categorie_list=Publication.objects.filter(categorie="Makeup steps")
    paginator = Paginator(categorie_list, 5)
    page = request.GET.get('page',1)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/steps.html',locals())

def BlackSkin(request):
    categorie_list=Publication.objects.filter(categorie="Makeup peau noire")
    paginator = Paginator(categorie_list, 5)
    page = request.GET.get('page',1)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/black.html',locals())

def WhiteSkin(request):
    categorie_list=Publication.objects.filter(categorie="Makeup peau claire")
    paginator = Paginator(categorie_list, 5)
    page = request.GET.get('page',1)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/white.html',locals())

def Soft(request):
    categorie_list=Publication.objects.filter(categorie="Makeup soft")
    paginator = Paginator(categorie_list, 5)
    page = request.GET.get('page',1)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/soft.html',locals())

def Soiree(request):
    categorie_list=Publication.objects.filter(categorie="Makeup soirée")
    paginator = Paginator(categorie_list, 5)
    page = request.GET.get('page',1)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/soiree.html',locals())

def Conseils(request):
    categorie_list=Publication.objects.filter(categorie="Conseils beauté")
    paginator = Paginator(categorie_list, 5)
    page = request.GET.get('page',1)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    last_threes = Publication.objects.all().order_by('-id')[:3][::1]
    count1=Publication.objects.filter(categorie="Makeup steps").count()
    count2=Publication.objects.filter(categorie="Makeup peau noire").count()
    count3=Publication.objects.filter(categorie="Makeup peau claire").count()
    count4=Publication.objects.filter(categorie="Makeup soft").count()
    count5=Publication.objects.filter(categorie="Makeup soirée").count()
    count6=Publication.objects.filter(categorie="Conseils beauté").count()
    return render(request,'Blog/conseil.html',locals())
