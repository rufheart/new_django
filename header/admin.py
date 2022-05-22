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


@admin.register(Detail_Product)
class DetailProduct(admin.ModelAdmin):
    inlines = [ImagesAdmin]

admin.site.register([Product,Cont_Info,Add_To_Card])

