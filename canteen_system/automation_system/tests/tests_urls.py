from django.test import TestCase
from django.urls import resolve, reverse
from automation_system.views import Logout, login_user,home, cart, contact_us, profile, menu, savereview, tocart, orders, savecart ,paycart, register, savereview, ownermenu, payconfirm

class Test_Urls(TestCase):
    
    def test_login(self):
        self.assertEquals(resolve("/").func, login_user)

    def test_register(self):
        self.assertEquals(resolve("/register").func, register)
    
    def test_logout(self):
        self.assertEquals(resolve("/logout").func, Logout)
    
    def test_home(self):
        self.assertEquals(resolve("/home").func, home)

    def test_profile(self):
        self.assertEquals(resolve("/home/profile").func, profile)

    def test_menu(self):
        self.assertEquals(resolve("/home/1").func, menu)
        self.assertEquals(resolve("/home/5").func, menu)
        self.assertNotEquals(resolve("/home/3/1").func, menu)

    def test_contactUs(self):
        self.assertEquals(resolve("/home/contact_us").func, contact_us)

    def test_cart(self):
        self.assertEquals(resolve("/home/cart").func, cart)
        self.assertEquals(resolve("/home/3/4433").func, tocart )
        self.assertEquals(resolve("/home/cart/paycart/1").func, paycart )
        self.assertEquals(resolve("/home/cart/443").func, savecart )
    
    def test_orders(self):
        self.assertEquals(resolve("/home/orders").func, orders)

    def test_review(self):
        self.assertEquals(resolve("/home/review/1").func, savereview)
    
    def test_ownermenu(self):
        self.assertEquals(resolve("/owner/1/3/6").func, ownermenu)
    
    def test_payconfirm(self):
        self.assertEquals(resolve("/payconfirm/0/11").func, payconfirm)
    
        