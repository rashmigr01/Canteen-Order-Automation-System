from django.db import models
from django.contrib.auth.models import User

class UserExt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.IntegerField(null=True)
    phone = models.BigIntegerField(null=True)
    isStaff = models.BooleanField(null=True)

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
    hall = models.IntegerField(null=True)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField
    dt = models.IntegerField(null=True)
    paymode = models.CharField(max_length= 1)
    paystatus = models.CharField(max_length= 1)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
