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
