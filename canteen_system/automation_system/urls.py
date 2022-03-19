from unicodedata import name
from django.urls import path

from . import views
from .models import UserExt

app_name = "auto"

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_user, name= "login"),
    path('logout', views.Logout, name= "logout")
]

