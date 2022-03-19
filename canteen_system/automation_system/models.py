from django.db import models
from django.contrib.auth.models import User

class UserExt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.IntegerField(null=True)
    phone = models.BigIntegerField(null=True)
    isStaff = models.BooleanField(null=True)


class MenuItem(models.Model):
    hall = models.CharField(null=True, max_length=10)
    item = models.CharField(null=True, max_length=50)
    price = models.IntegerField(null=True)
    avail = models.BooleanField(null=True)
    isveg = models.BooleanField(null=True)
    rating = 

class Orders(models.Model):
    Hall = models.IntegerField
    Item = models.CharField
    Quantity = models.IntegerField
    D_T = models.CharField(max_length= 1)
    PayMode = models.CharField(max_length= 1)
    PayStatus = models.CharField(max_length= 1)
    Customer = models.ForeignKey(UserExt, on_delete = models.CASCADE)
    # OrderNo = models.IntegerField

    # def save(self):
    #     self.OrderNo = 100* self.Customer.roll + self.

class Reviews(models.Model):
     Reviewer = models.ManyToManyField("UserExt")
     Rating = models.IntegerField
     TextMessage = models.CharField(max_length = 200)
     order = models.OneToOneField(Orders, 
          on_delete = models.CASCADE, primary_key = True)
