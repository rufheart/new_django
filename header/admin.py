from django.contrib import admin
from header.models import Category, Product, Product_Detail, Images, Review, Add_To_Card

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


@admin.register(Product_Detail)
class DetailProduct(admin.ModelAdmin):
    inlines = [ImagesAdmin]

admin.site.register([Product, Review, Add_To_Card])

