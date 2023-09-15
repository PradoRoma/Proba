"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from firstapp import views
from django.views.generic import TemplateView


urlpatterns = [
    path('abouts/', TemplateView.as_view(template_name="about.html", 
        extra_context={"about": "О сайте"})),
    path('contacts/', TemplateView.as_view(template_name="contact.html",
        extra_context={"contact":"Контакты"})),
    path('products/<int:productid>/', views.products),
    path('users/', views.users),
    #re_path(r'^products/$', views.product),
    #re_path(r'^users/$', views.users),
    #re_path(r'^products/(?P<productid>\d+)/', views.product),
    #path('users/<int:id>/<name>/', views.users),
    #re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    #re_path(r'^about/contact', views.contact),
    #re_path(r'^about', views.about),
    path('details/', views.details),
    path('contact/', views.contact),
    path('about/', views.about),
    path('', views.index),
    path('admin/', admin.site.urls),
]
