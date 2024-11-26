
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('miusica',views.miusician,name='miusica'),
    path('album',views.album,name='album')
]
