from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import MenuItem, Order, Review, UserExt


admin.site.register(UserExt)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(Review)
