from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import UserExt
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("HomePage for Automation System.")

def register(request):
    if request.method == "POST":
        user = User( username = request.POST["usern"], email = request.POST["email"], password= request.POST["passw"])
        user.save()

        print(int(request.POST["roll"]))

        userEx = UserExt(user = user)
        print(userEx.__dict__)
        userEx.save()
        userEx.roll = int(request.POST["roll"])
        userEx.phone = int(request.POST["phone"])
        userEx.isStaff = True if request.POST["isStaff"] == "True" else False
        userEx.save()
        print(userEx.__dict__)
        print("This ran")
    return render(request, 'home/register.html')
