import imp
from turtle import update
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import MenuItem, Order, UserExt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("auto:home"))
    if request.method == "POST":
        user = User.objects.create_user(username = request.POST["usern"], email = request.POST["email"], password= request.POST["passw"])
        #user = User( username = request.POST["usern"], email = request.POST["email"], password= request.POST["passw"])
        user.save()

        print(int(request.POST["roll"]))

        userEx = UserExt(user = user, roll = int(request.POST["roll"]), phone = int(request.POST["phone"]), isStaff = True if request.POST["isStaff"] == "True" else False)
        userEx.save()

        login(request, user)
        return HttpResponseRedirect(reverse("auto:home"))
        # messages.success(request,'You are Regestered Successfully!!')
    return render(request, 'home/registration.html')

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("auto:home"))
    if request.method =="POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("auto:home"))
        else:
            return HttpResponse("Ex occured")

    return render(request, 'home/login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("auto:login"))

def home(request):
    context = {"username" : request.user.username}
    return render(request, 'home/home.html', context)

def profile(request):
    context = {
        'ext' : UserExt.objects.get(user = request.user)
        }
    return render(request, 'home/profile.html', context)

def menu(request, hall):
    items = MenuItem.objects.filter(hall = hall)
    context = {'items':items}
    return render(request, 'home/menu.html', context)