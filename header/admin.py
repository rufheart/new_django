from faulthandler import disable
from django.contrib import admin
from header.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", 'parent_id']
    fields = ('title', 'parent_id')
    search_fields = ('title', )
    list_filter = ('title', )


