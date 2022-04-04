from django.contrib import admin
from header.models import Contact, Product, Tag, Images,Cont_Info


# class ImagesAdmin(admin.TabularInline):
#     model = Images
#     fields = ('picture', )

@admin.register(Product)
class product(admin.ModelAdmin):
    list_display = ['name','new_pr']
    search_fields = ['name']
    list_filter = ['tag']
    # inlines = [ImagesAdmin]

admin.site.register([Contact,Tag, Images,Cont_Info])
