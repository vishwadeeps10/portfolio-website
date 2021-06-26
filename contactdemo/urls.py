
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('contact', views.contactform , name='contact' ),
    path('', views.homepage , name='homepage' ),
    path('about', views.about , name='about' ),
    path('project', views.project , name='project' ),
   
]
