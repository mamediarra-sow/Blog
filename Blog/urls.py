"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from MonBlog import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.AboutPage, name='AboutPage'),
    path('home/', views.HomePage, name='HomePage'),
    path('blog-single/<int:id>', views.SingleBlogPage, name='SingleBlogPage'),
    path('blog/', views.BlogPage, name='BlogPage'),
    path('contact/', views.ContactPage, name='ContactPage'),
    path('login/', views.Login, name="Login"),
    path('like/<int:id>',views.LikePost, name="LikePost"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
