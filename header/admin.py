from django.contrib import admin
from header.models import Contact, Product, Tag,Cont_Info,Images,Review


class ImagesAdmin(admin.TabularInline):
    model = Images
    fk_name = "products"
    fields = ('images_tb', )

@admin.register(Product)
class product(admin.ModelAdmin):
    list_display = ['name','new_pr']
    search_fields = ['name']
    list_filter = ['tag']
    inlines = [ImagesAdmin]

@admin.register(Cont_Info)
class cont_inf(admin.ModelAdmin):
    list_display = ['fname','country']

admin.site.register([Contact,Tag,Review])
