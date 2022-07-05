from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from header.models import Product, Detail_Product
from account.models import User
from django.contrib.auth.hashers import make_password

# class CategorySerialize(serializers.ModelSerializer):
#     class Meta:
#         model=Category
#         fields = ('id','title')

class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username','first_name','last_name', 'email', 'password']       


    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
