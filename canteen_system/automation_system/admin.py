from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import MenuItem, UserExt


admin.site.register(UserExt)
admin.site.register(MenuItem)
