from django.contrib import admin
from header.models import Contact, Product, Tag, Images

# Register your models here.

admin.site.register([Contact, Product, Tag, Images])
