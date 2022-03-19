from turtle import update
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import UserExt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == "POST":
        user = User.objects.create_user(username = request.POST["usern"], email = request.POST["email"], password= request.POST["passw"])
        #user = User( username = request.POST["usern"], email = request.POST["email"], password= request.POST["passw"])
        user.save()

        print(int(request.POST["roll"]))

        userEx = UserExt(user = user, roll = int(request.POST["roll"]), phone = int(request.POST["phone"]), isStaff = True if request.POST["isStaff"] == "True" else False)
        userEx.save()
        # messages.success(request,'You are Regestered Successfully!!')
    return render(request, 'home/registration.html')

def login_user(request):
    if request.method =="POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return HttpResponse("Logged In")
        else:
            return HttpResponse("Ex occured")

    return render(request, 'home/login.html')

def Logout(request):
    logout(request)
    return HttpResponse("Logged Out.")