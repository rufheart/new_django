from django.contrib import admin
from header.models import Contact, Product

# Register your models here.

admin.site.register([Contact, Product])
