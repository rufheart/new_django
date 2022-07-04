from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from header.models import Product, Detail_Product
from account.models import User

# class CategorySerialize(serializers.ModelSerializer):
#     class Meta:
#         model=Category
#         fields = ('id','title')

class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username','first_name','last_name', 'email', 'password']       

