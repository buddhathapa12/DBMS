from django.conf.urls import url 
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index , name= 'index'),
    path('search/', views.search,name = 'search'),
]