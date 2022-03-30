from django.contrib import admin
from header.models import Contact, Product, Tag, Images

# Register your models here.

@admin.register(Product)
class product(admin.ModelAdmin):
    list_display = ['name','new_pr']
    search_fields = ['name']
    list_filter = ['tag']

admin.site.register([Contact,Tag, Images])
