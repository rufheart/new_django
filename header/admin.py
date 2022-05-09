from django.contrib import admin
from header.models import Contact, Product,Cont_Info,Images,Review, Add_To_Card, Category


class ImagesAdmin(admin.TabularInline):
    model = Images
    fk_name = "products"
    fields = ('images_tb', )

@admin.register(Product)
class product(admin.ModelAdmin):
    list_display = ['name','new_pr']
    search_fields = ['name']
    list_filter = []
    inlines = [ImagesAdmin]

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_filter = ['title']  

@admin.register(Cont_Info)
class cont_inf(admin.ModelAdmin):
    list_display = ['fname','country']

admin.site.register([Contact,Review, Add_To_Card])
