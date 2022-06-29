from dataclasses import fields
from rest_framework import serializers
from header.models import Product, Detail_Product

# class CategorySerialize(serializers.ModelSerializer):
#     class Meta:
#         model=Category
#         fields = ('id','title')
        

class ProductSerialize(serializers.ModelSerializer):
    # category_pro = CategorySerialize()
    class Meta:
        model=Product
        fields = ('id','user','category_pro','name') 

class DetailSerialize(serializers.ModelSerializer):
    detail = ProductSerialize()
    class Meta:
        model = Detail_Product
        fields = ('id','detail','image', 'desc', 'new_pr', 'old_pr','slug')

class CreateSerialize(serializers.ModelSerializer):
    class Meta:
        model = Detail_Product
        fields = ('detail','image', 'desc', 'new_pr', 'old_pr')        