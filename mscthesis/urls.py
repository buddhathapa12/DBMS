from django.conf.urls import url 
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mscthesis.views import SearchView
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index , name= 'index'),
    path('login/',views.login_view, name = 'login_view'),
    path('logout/',views.logout_view,name = 'logout_view'),
    path('signup/',views.signup_view,name = 'signup_view'),

    path('search/',SearchView.as_view(),name = 'search'),
]