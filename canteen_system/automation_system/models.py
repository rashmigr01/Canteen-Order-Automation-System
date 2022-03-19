from django.db import models
from django.contrib.auth.models import User

class UserExt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.IntegerField(null=True)
    phone = models.BigIntegerField(null=True)
    isStaff = models.BooleanField(null=True)
