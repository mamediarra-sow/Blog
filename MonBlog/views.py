from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request,'Blog/index.html')

def AboutPage(request):
    return render(request,'Blog/about.html')

def SingleBlogPage(request):
    return render(request,'Blog/blog-single.html')

def BlogPage(request):
    return render(request,'Blog/blog.html')

def ContactPage(request):
    return render(request,'Blog/contact.html')

def GalleryPage(request):
    return render(request,'Blog/gallery.html')

def ServicesPage(request):
    return render(request,'Blog/services.html')

