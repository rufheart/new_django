from django.db import models
from django.shortcuts import render

# Create your models here.

class ABS(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class meta():
        abstract = True

class Contact(ABS):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    company = models.CharField(max_length=40)
    tel = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    comment = models.TextField()

    def __str__(self) -> str:
        return self.name


class Tag(ABS):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Product(ABS):
    name=models.CharField(max_length=35)
    tag = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to = 'img/product/')
    desc = models.TextField()
    new_pr=models.CharField(max_length=10)
    old_pr=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class Images(ABS):
    haqq = models.ForeignKey(Product,related_name='images', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to = 'img/images/') 
    

    



















































    
                

