from dataclasses import fields
from rest_framework import serializers
from header.models import Product, Category

class CategorySerialize(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ('id','title')
        

class ProductSerialize(serializers.ModelSerializer):
    category = CategorySerialize()
    class Meta:
        model=Product
        fields = ('id','category_pro','name') 
