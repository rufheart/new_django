from django.contrib import admin
from header.models import Category, Product, Product_Detail

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", 'parent_id']
    fields = ('title', 'parent_id')
    search_fields = ('title', )
    list_filter = ('title', )

admin.site.register(Product)
admin.site.register(Product_Detail)
