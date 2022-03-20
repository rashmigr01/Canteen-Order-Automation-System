from http import client
from urllib import response
from django.test import TestCase, Client
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from automation_system.views import Logout, login_user,home, cart, contact_us, profile, menu, tocart, orders, savecart ,paycart, register
from automation_system.models import MenuItem, Order, UserExt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class TestViews(TestCase):

    def setUp(self):
        client = Client()

        user = User.objects.create_user(
            username = "user1", 
            email = "user1@gmail.com", 
            password= "user1")

        userEx = UserExt.objects.create(
            user = user, 
            roll = 234, 
            phone = 999999999, 
            isStaff = True )

        Dish = MenuItem.objects.create(
            hall = 6,
            item = "Salad",
            price = 10,
            avail = True,
            isveg = True)

        order = Order.objects.create(
            hall = 6,
            item = Dish,
            quantity = 3,
            dt = 1,
            paymode = 1,
            paystatus = 1,
            user = userEx
        )

    def test_user_login_Post(self):
        response1 = self.client.post(
            '',{'username' : 'user1','password' : 'user1'}
        )
        self.assertEquals(response1.status_code, 302) #redirected
        #self.assertEquals(response1,HttpResponseRedirect(reverse("auto:home")))
        #self.assertIn(b'<h2>Motivation</h2>', response1.content)
        response2 = self.client.post(
            '',{'username' : 'user1','password' : 'user672'}
        )
        self.assertEquals(response2.status_code, 302) #not authenticated
        self.assertEquals(response2 ,HttpResponse("Ex occured"))
    
    # def test_profile_page(self):
    #     request = HttpRequest()
    #     response = profile(request)
    #     self.assertIn(b'<h3 class="mt-3 text-center">Profile</h3>', response.content)


    