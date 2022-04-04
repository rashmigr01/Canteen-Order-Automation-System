from automation_system.models import MenuItem, Order, Review, UserExt
from django.contrib.auth.models import User
from django.test import TestCase

class TestModels(TestCase):
    
    def test_basic(self):
        #record_user = UserExt.objects.get(pk =1)
        user = User.objects.create_user(
            username = "user1", 
            email = "user1@gmail.com", 
            password= "user1")

        userEx = UserExt.objects.create(
            user = user, 
            roll = 234, 
            phone = 999999999, 
            isStaff = True )

        Dish1 = MenuItem.objects.create(
            hall = 6,
            item = "Salad",
            price = 10,
            avail = True,
            isveg = True)
        Dish2 = MenuItem.objects.create(
            hall = 6,
            item = "Milk",
            price = 10,
            avail = True,
            isveg = True)

       

        review = Review.objects.create(
            user = userEx,
            rating = 3,
            #textmess = " ",
            item = Dish1
        )
        
        record_menuItem = MenuItem.objects.get(pk =2)
        self.assertEqual(record_menuItem, Dish2)
        self.assertEqual(Order.objects.all().count(),0)
        self.assertIn(review, Review.objects.filter(rating=3))
        self.assertIn(userEx, UserExt.objects.filter(isStaff = True))

    def test_display_name(self):
        user = User.objects.create_user(
            username = "user1", 
            email = "user1@gmail.com", 
            password= "user1")

        userEx = UserExt.objects.create(
            user = user, 
            roll = 234, 
            phone = 999999999, 
            isStaff = True )
       
        Dish1 = MenuItem.objects.create(
            hall = 6,
            item = "Salad",
            price = 10,
            avail = True,
            isveg = True)
        order1 = Order.objects.create(
            hall = 6,
            item = Dish1,
            quantity = 3,
            dt = 1,
            paymode = 1,
            paystatus = 1,
            user = userEx
        )
        review = Review.objects.create(
            user = userEx,
            rating = 3,
            #textmess = " ",
            item = Dish1
        )
        self.assertEqual(Dish1.item, Dish1.__str__())
        self.assertEqual(userEx.user.username, userEx.__str__())
        self.assertEqual("%s - %s" % (order1.item, order1.quantity), order1.__str__())
        self.assertEqual("%s - %s" % (review.item, review.user.user.username), review.__str__())
        
        
