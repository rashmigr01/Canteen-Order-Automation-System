import imp
import re
from turtle import update
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import MenuItem, Order, Review, UserExt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("auto:home"))
    if request.method == "POST":
        
        a = User.objects.filter(username = request.POST["usern"])

        if(len(a) > 0):
            context = {
                'error' : 1
            }
            return render(request, 'home/registration.html', context)
        
        user = User.objects.create_user(username = request.POST["usern"], email = request.POST["email"], password= request.POST["passw"])
        user.save()


        userEx = UserExt(user = user, roll = int(request.POST["roll"]), phone = int(request.POST["phone"]), isStaff = False, hall= int(request.POST["hall"]))
        userEx.save()

        login(request, user)
        return HttpResponseRedirect(reverse("auto:home"))
    return render(request, 'home/registration.html')

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("auto:home"))
    if request.method =="POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("auto:home"))
        else:
            context = {
                'error' : 1
            }
            return render(request, 'home/login.html',context)

    return render(request, 'home/login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("auto:login"))

def home(request):
    context = {
        "username" : request.user.username,
        "staff" : UserExt.objects.get(user = request.user).isStaff
        }
    return render(request, 'home/home.html', context)

def profile(request):
    context = {
        'ext' : UserExt.objects.get(user = request.user),
        "username" : request.user.username,
        "staff" : UserExt.objects.get(user = request.user).isStaff
        }
    return render(request, 'home/profile.html', context)

def menu(request, hall):

    rat = []

    if UserExt.objects.get(user = request.user).isStaff == False:
        items = MenuItem.objects.filter(hall = hall)
        for item in items:
            avg = {'rating' : 0}
            it = Review.objects.filter(item = item)
            for i in it:
                avg['rating'] += i.rating
            avg['rating'] = (avg['rating']/len(it)) if len(it) > 0 else " --- "
            rat.append(avg)

        context = {
            'hall': hall,
            'items':items,
            'ratings': rat,
            "username" : request.user.username,
            "staff" : UserExt.objects.get(user = request.user).isStaff
            }
        return render(request, 'home/menu.html', context)
    else:
        items = MenuItem.objects.filter(hall = UserExt.objects.get(user = request.user).hall)
        for item in items:
            avg = {'rating' : 0}
            it = Review.objects.filter(item = item)
            for i in it:
                avg['rating'] += i.rating
            avg['rating'] = (avg['rating']/len(it)) if len(it) > 0 else " --- "
            rat.append(avg)

        context = {
            'hall': UserExt.objects.get(user = request.user).hall,
            'items': items,
            'ratings': rat,
            "username" : request.user.username,
            "staff" : UserExt.objects.get(user = request.user).isStaff
            }
        return render(request, 'home/menu_owner.html', context)

def orders(request):
    if UserExt.objects.get(user = request.user).isStaff == False:
        ords = Order.objects.filter(user = UserExt.objects.get(user = request.user)).exclude(paystatus = 1).order_by('-id')    
        
        revs = []
        
        for i in ords:
            rev = Review.objects.filter(user = UserExt.objects.get(user = request.user), item = i.item)
            rev = rev[0] if len(rev) >0 else rev
            revs.append(rev)


        tot = []
        tf = 0
        for j in range(1,14):
            p = 0
            for i in ords:
                if i.item.hall == j:
                    if i.paystatus == 2 or i.paystatus ==3:
                        t = i.item.price* i.quantity
                        tf = tf + t
                        p = p + t
            tot.append(p)

        context = {
            'full_total' : tf,
            'orders' : zip(ords,revs),
            'total' : tot,
            "username" : request.user.username,
            "staff" : UserExt.objects.get(user = request.user).isStaff
        }
        return render(request, 'home/orders.html', context)

    else:
        ords = Order.objects.filter(hall = UserExt.objects.get(user = request.user).hall, deli = False)

        context = {
            'orders' : ords,
            "username" : request.user.username,
            "staff" : UserExt.objects.get(user = request.user).isStaff
        }

        return render(request, 'home/pending_orders.html', context)

def tocart(request,hall, itemId):
    item = MenuItem.objects.get(id=int(itemId))
    order = Order(hall = hall, item = item, quantity = 1, dt = 0, paymode = 0, paystatus=0, user = UserExt.objects.get(user = request.user))
    order.save()
    return HttpResponseRedirect(reverse('auto:menu', args=(hall,)))

def savecart(request, orderId):
    if request.method == "POST":
        order = Order.objects.get(id = orderId)
        if int(request.POST['quant']) <= 0:
            order.delete()
        else:
            order.quantity = int(request.POST['quant'])
            order.save()

    return HttpResponseRedirect(reverse('auto:cart'))

def savereview(request, itemId):
    rev = Review.objects.filter(user = UserExt.objects.get(user = request.user), item = MenuItem.objects.get(id = itemId))
    if len(rev) != 0:
        rev[0].rating = int(request.POST['rate'])
        rev[0].save()
    else:
        rev = Review(user = UserExt.objects.get(user = request.user), rating = int(request.POST['rate']), item =  MenuItem.objects.get(id = itemId))
        rev.save()

    return HttpResponseRedirect(reverse('auto:orders'))

def cart(request):
    ords = Order.objects.filter(user = UserExt.objects.get(user = request.user), paystatus = 0)
    lis = []
    tot = 0
    for i in ords:
        di = {}
        t = i.item.price* i.quantity
        di['name'] = i.item.item
        di['cost'] = t
        tot+= t
        lis.append(di)

    context = {
        'orders' : ords,
        'costs' : lis,
        'total' : tot,
        "username" : request.user.username,
        "staff" : UserExt.objects.get(user = request.user).isStaff
    }
    return render(request, 'home/cart.html', context)

def paycart(request, paystat):
    ords = Order.objects.filter(user = UserExt.objects.get(user = request.user), paystatus = 0)
    
    for i in ords:
        if int(paystat) == 1:
            i.paystatus = 1
        elif int(paystat) == 2:
            i.paystatus = 2
        elif int(paystat) == 3:
            i.paystatus = 3
        else:
            i.paystatus = 0
        i.save()

    return HttpResponseRedirect(reverse('auto:orders'))

def ownermenu(request, stat, itemId, hall):

    if request.method == "GET":
        it = MenuItem.objects.get(id = int(itemId))
        it.delete()
        return HttpResponseRedirect(reverse('auto:menu', args=(hall,) ))

     # 0 for edit, 1 for add and 2 for delete

    if int(stat) == 0:
        it = MenuItem.objects.get(id = int(itemId))
        po = request.POST
        it.item = po['item']
        it.price = int(po['price'])
        it.avail = True if po['avail'] == '1' else False
        it.isveg = True if po['isveg'] == '1' else False

        it.save()

    else:
        po = request.POST
        it = MenuItem(hall = UserExt.objects.get(user = request.user).hall, item = po['item'], price = int(po['price']), avail = True if po['avail'] == '1' else False, isveg = True if po['isveg'] == '1' else False)
        it.save()
    
    return HttpResponseRedirect(reverse('auto:menu', args=(hall,) ))

def payconfirm(request,stat, orderId):
    # print("Payconfirm", stat, orderId)
    ord = Order.objects.get(id = orderId)
    # 0 for paid and 1 for done
    if int(stat) == 0:
        ord.paystatus = 1
        ord.save()
    else:
        ord.deli = True
        ord.save()

    return HttpResponseRedirect(reverse('auto:orders'))

def contact_us(request):
    context = {
        "username" : request.user.username,
        "staff" : UserExt.objects.get(user = request.user).isStaff
        }
    return render(request, 'home/contact_us.html', context)

def user_due(request):

    users = UserExt.objects.filter(isStaff = False)

    use = []
    cost = []

    for i in users:
        ords = Order.objects.filter(user = i, hall = UserExt.objects.get(user = request.user).hall).exclude(paystatus = 1).order_by('-id')    
        tot = 0
        for j in ords:
            t = j.item.price* j.quantity
            if j.paystatus == 2 or j.paystatus ==3:
                tot+= t
            
        if tot > 0:
            use.append(i)
            cost.append(tot)

    context = {
        "username" : request.user.username,
        "staff" : UserExt.objects.get(user = request.user).isStaff,
        "zipped" : zip(use,cost)
    }
    return render(request, 'home/user_due.html', context)

def completed_orders(request):
    ords = Order.objects.filter(hall = UserExt.objects.get(user = request.user).hall, deli = True)

    context = {
        'orders' : ords,
        "username" : request.user.username,
        "staff" : UserExt.objects.get(user = request.user).isStaff
    }

    return render(request, 'home/completed_orders.html', context)