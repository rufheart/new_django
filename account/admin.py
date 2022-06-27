from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User


class User_Admin(UserAdmin):
    pass



# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass

admin.site.register(User, User_Admin)