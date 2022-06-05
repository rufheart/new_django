from django.contrib import admin
from header.models import Category, Product, Detail_Product , Images, Review, Add_To_Card,Cont_Info

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", 'parent_id']
    fields = ('title', 'parent_id')
    search_fields = ('title', )
    list_filter = ('title', )


class ImagesAdmin(admin.TabularInline):
    model = Images
    fk_name = "productsdetail"
    fields = ('images_tb', )


# @admin.register(Detail_Product)
# class DetailProduct(admin.ModelAdmin):
#     inlines = [ImagesAdmin]

class DetailProduct(admin.TabularInline):
    model=Detail_Product
    fk_name = "detail"
    fields = ['detail','image','desc','new_pr','old_pr']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    inlines = [DetailProduct]    

admin.site.register([Cont_Info,Add_To_Card])

