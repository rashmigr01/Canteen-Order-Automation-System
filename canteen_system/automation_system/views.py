from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import UserExt
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("HomePage for Automation System.")

def register(request):
    if request.method == "POST":
        user = User.objects.create(request.POST["usern"], request.POST["email"], request.POST["passw"])
        user.save()
        userEx = UserExt.objects.create(user,int(request.POST["roll"]), int(request.POST["phone"]),request.POST["isStaff"])
        userEx.save()
        print("This ran")
    return render(request, 'home/register.html')
