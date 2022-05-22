from pyexpat import model
from unicodedata import category
from django.db import models 
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

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


class Category(ABS):
    title = models.CharField(max_length=50)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Product(ABS):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE,null=True)
    category_pro = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.name

class Detail_Product(ABS):
    detail = models.ForeignKey(Product, related_name='product_det', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'img/product')
    desc = models.CharField(max_length=50)
    new_pr = models.CharField(max_length=10)
    old_pr = models.CharField(max_length=10)
    slug = models.SlugField(blank=True, null = True, unique=True)

    def __str__(self) -> str:
        return str(self.detail)
        
class Images(ABS):
    productsdetail = models.ForeignKey(Detail_Product, related_name='images', on_delete=models.CASCADE)
    images_tb = models.ImageField(upload_to = 'img/product/images ') 
    

class PropertyName(ABS):
    name = models.CharField(max_length=40)
    category_base = models.ForeignKey(Category, related_name='propertyname', on_delete=models.CASCADE)


class PropertyValues(ABS):
    name = models.CharField(max_length=50)
    property_name = models.ForeignKey(PropertyName, related_name='propertyvalues', on_delete=models.CASCADE)    
    product_detail = models.ManyToManyField(Detail_Product, db_table='ProductPropertiesValues')



class Cont_Info(ABS):
    fname = models.CharField(max_length=35)
    lname=models.CharField(max_length=35)
    company=models.CharField(max_length=50)
    tel=models.CharField(max_length=13)
    fax=models.CharField(max_length=30)
    s_address=models.CharField(max_length=50)
    s_2address=models.CharField(max_length=50)
    city=models.CharField(max_length=35)
    state=models.SmallIntegerField(choices=((1,'Alabama'),(2,'Alaska'),(3,'Arizona')))
    zip=models.CharField(max_length=25)  
    country=models.SmallIntegerField(choices=((1,'Azerbaijan'),(2,'Afganistan')))
    bil_addr=models.BooleanField()
    ship_addr=models.BooleanField()


    def __str__(self) -> str:
        return self.fname


class Review(ABS):
    user_pro = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE)
    product_review = models.ForeignKey(Product, related_name="Review", on_delete=models.CASCADE)
    value_review = models.SmallIntegerField('Value', choices=((1,'1'),(2,'2'), (3,'3'), (4,'4'), (5,'5')), default=0)
    quality_review = models.SmallIntegerField('Quality', choices=((1,'1'),(2,'2'), (3,'3'), (4,'4'), (5,'5')), default=0)
    price_review = models.SmallIntegerField('Price', choices=((1,'1'),(2,'2'), (3,'3'), (4,'4'), (5,'5')), default=0)
    summary = models.CharField('Summary',max_length=40)
    comment = models.TextField()


class Add_To_Card(ABS):
    add_product=models.ForeignKey(Product, related_name='add_to_card', on_delete=models.CASCADE, null=True)
    add_usr = models.ForeignKey(User, related_name='add_to_card', on_delete=models.CASCADE)











































    
                

