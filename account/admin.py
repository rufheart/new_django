from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User


class User_Admin(UserAdmin):
    pass

admin.site.register(User,User_Admin)