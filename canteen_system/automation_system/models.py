from itertools import count
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserExt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.IntegerField(null=True)
    phone = models.BigIntegerField(null=True)
    isStaff = models.BooleanField(null=True)
    hall = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.user.username


class MenuItem(models.Model):
    hall = models.IntegerField(null=True)
    item = models.CharField(null=True, max_length=50)
    price = models.IntegerField(null=True)
    avail = models.BooleanField(null=True)
    isveg = models.BooleanField(null=True)

    def __str__(self) -> str:
        return self.item


class Order(models.Model):

    '''
    Payment Status
    1: Paid
    2: Unpaid
    3: Waiting
    '''

    hall = models.IntegerField(null=True)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    dt = models.IntegerField(null=True)
    paymode = models.IntegerField(null=True)
    paystatus = models.IntegerField(null=True)
    user = models.ForeignKey(UserExt, on_delete=models.CASCADE)
    DateOfOrder = models.DateField(auto_now_add=True, null=True)
    deli = models.BooleanField(null=True, default=False)

    @property
    def orderId(self):
        x = Order.objects.filter(DateOfOrder = datetime.now() ).count()
        return "%s/%s%s%s/%s" % (self.hall,self.DateOfOrder.strftime("%Y"),self.DateOfOrder.strftime("%m"),self.DateOfOrder.strftime("%d"),x)
        

    def __str__(self) -> str:
        return "{} - {}".format(self.item.item, self.quantity)

class Review(models.Model):
    user = models.ForeignKey(UserExt, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True,default=0)
    item = models.ForeignKey(MenuItem, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return "{} - {}".format(self.item.item ,self.user.user.username)
