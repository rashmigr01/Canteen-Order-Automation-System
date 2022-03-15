from django.urls import path

from . import views

app_name = "auto"

urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.register, name='register')
]

