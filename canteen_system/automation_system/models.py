from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

class UserExt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.IntegerField
    phone = models.BigIntegerField
    isStaff = models.BooleanField

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)

class Review(models.Model):
    srn = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = GenericRelation(Rating)
    timestamp = models.DateTimeField(default=now)