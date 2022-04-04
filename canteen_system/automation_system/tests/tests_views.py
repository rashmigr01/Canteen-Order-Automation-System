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
            isStaff = False )

        Dish = MenuItem.objects.create(
            hall = 6,
            item = "Salad",
            price = 10,
            avail = True,
            isveg = True)
        
        order0 = Order.objects.create(
            hall = 6,
            item = Dish,
            quantity = 2,
            dt = 1,
            paymode = 0,
            paystatus = 0,
            user = userEx
        )
        order1 = Order.objects.create(
            hall = 6,
            item = Dish,
            quantity = 3,
            dt = 1,
            paymode = 1,
            paystatus = 1,
            user = userEx
        )
        order2 = Order.objects.create(
            hall = 6,
            item = Dish,
            quantity = 1,
            dt = 1,
            paymode = 1,
            paystatus = 2,
            user = userEx
        )
        order3 = Order.objects.create(
            hall = 6,
            item = Dish,
            quantity = 1,
            dt = 1,
            paymode = 1,
            paystatus = 3,
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
         self.assertIn(b'<h6 class="text-muted">user2@gmail.com</h6>', response.content)

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

    def test_order_unpaid_total(self):
        response1 = self.client.post(
            '',{'username' : 'user1' ,'password' : 'user1'}
        )
        response = self.client.get('/home/orders')
        self.assertIn(b'20', response.content)
        self.assertIn(b'Quantity : 1',response.content)

    def test_cart_display_items(self):
        response1 = self.client.post(
            '',{'username' : 'user1' ,'password' : 'user1'}
        )
        response = self.client.get('/home/cart')
        self.assertIn(b'20', response.content)

    def test_contact_us(self):
        response1 = self.client.post(
            '',{'username' : 'user1' ,'password' : 'user1'}
        )
        response = self.client.get('/home/contact_us')
        self.assertEquals(response.status_code, 200)
        


    