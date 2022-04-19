from unicodedata import name
from django.urls import path

from . import views
from .models import UserExt

app_name = "auto"

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login_user, name= "login"),
    path('logout', views.Logout, name= "logout"),
    path('home', views.home, name='home'),
    path('home/profile', views.profile, name='profile'),
    path('home/<int:hall>', views.menu, name='menu'),
    path('home/<int:hall>/<int:itemId>', views.tocart, name='tocart'),
    path('owner/<int:stat>/<int:itemId>/<int:hall>', views.ownermenu, name='ownermenu'),
    path('payconfirm/<int:stat>/<int:orderId>', views.payconfirm, name='payconfirm'),
    path('home/cart/<int:orderId>', views.savecart, name='savecart'),
    path('home/review/<int:itemId>', views.savereview, name='savereview'),
    path('home/cart', views.cart, name='cart'),
    path('home/orders', views.orders, name='orders'),
    path('home/cart/paycart/<int:paystat>', views.paycart, name='paycart'),
    path('home/contact_us', views.contact_us, name='contact_us'),
    path('owner/user_due', views.user_due, name='user_due'),
    path('owner/completed_orders', views.completed_orders, name='completed_orders'),
]

