from http import client
from urllib import response
from django.test import TestCase, Client
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from automation_system.views import Logout, login_user,home, cart, contact_us, profile, menu, tocart, orders, savecart ,paycart, register
from automation_system.models import MenuItem, Order, UserExt, Review
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

        review1 = Review.objects.create(
            user = userEx,
            rating = 4,
            item = Dish
        )
        review2 = Review.objects.create(
            user = userEx,
            rating = 5,
            item = Dish
        )

    def test_user_login_Post(self):
        response1 = self.client.post(
            '',{'username' : 'user1','password' : 'user1'}
        )
        self.assertEquals(response1.status_code, 302) #redirected
        
    def test_user_login_Failure(self):
        response2 = self.client.post(
            '',{'username' : 'user1','password' : 'user672'}
        )
        self.assertEquals(response2.status_code, 200) #not authenticated
        
    
    def test_profile_page(self):
        #request = HttpRequest()
         user2 = User.objects.create_user(
            username = "user2", 
            email = "user2@gmail.com", 
            password= "user2")
         userEx2 = UserExt.objects.create(
            user = user2, 
            roll = 234, 
            phone = 999999999, 
            isStaff = True )
         response1 = self.client.post(
            '',{'username' : 'user2' ,'password' : 'user2'}
        )
         response = self.client.get('/home/profile',{ 'ext' : userEx2 })
         self.assertIn(b'<h3 class="mt-3 text-center">Profile</h3>', response.content)

    def test_ifStaff_access_menu(self):
         user2 = User.objects.create_user(
            username = "user2", 
            email = "user2@gmail.com", 
            password= "user2")
         userEx2 = UserExt.objects.create(
            user = user2, 
            roll = 234, 
            phone = 999999999, 
            isStaff = True )
         response1 = self.client.post(
            '',{'username' : 'user2' ,'password' : 'user2'}
        )
         response = self.client.get('/home/6',{ 'hall':6})
         self.assertIn(b'<label>Yes</label>', response.content)

    def test_ifNotStaff_access_menu(self):
         user2 = User.objects.create_user(
            username = "user2", 
            email = "user2@gmail.com", 
            password= "user2")
         userEx2 = UserExt.objects.create(
            user = user2, 
            roll = 234, 
            phone = 999999999, 
            isStaff = False )
         response1 = self.client.post(
            '',{'username' : 'user2' ,'password' : 'user2'}
        )
         response = self.client.get('/home/6',{ 'hall':6})
         self.assertIn(b'<h5 class="card-title">Salad</h5>', response.content)
        
    def test_rating_menu(self):
        user2 = User.objects.create_user(
            username = "user2", 
            email = "user2@gmail.com", 
            password= "user2")
        userEx2 = UserExt.objects.create(
            user = user2, 
            roll = 234, 
            phone = 999999999, 
            isStaff = False )
        response1 = self.client.post(
            '',{'username' : 'user2' ,'password' : 'user2'}
        )
        response = self.client.get('/home/6',{ 'hall':6})
        self.assertIn(b'<p class="card-text">Averate Rating : 4.5</p>', response.content)

    
        


    