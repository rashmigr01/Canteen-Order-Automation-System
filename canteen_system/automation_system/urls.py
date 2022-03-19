from unicodedata import name
from django.urls import path

from . import views
from .models import UserExt

app_name = "auto"

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login_user, name= "login"),
    path('logout', views.Logout, name= "logout")
]

