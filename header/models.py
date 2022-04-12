import django
from django.db import models 
from django.shortcuts import render
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


class Tag(ABS):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Product(ABS):
    name = models.CharField(max_length=35)
    tag = models.ManyToManyField(Tag, related_name='Product', blank=True)
    image = models.ImageField(upload_to = 'img/product')
    desc = models.TextField()
    new_pr=models.CharField(max_length=10)
    old_pr=models.CharField(max_length=10)
    slug = models.SlugField(null=False, blank=True, unique=True)

 
    def save(self, *args, ** kwargs):
        self.slug = slugify(self.desc+self.old_pr+self.new_pr)
        print('form.save.isledi')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Review(ABS):
    user = models.ForeignKey(User, related_name='Rewiew', on_delete=models.CASCADE)
    product_revi = models.ForeignKey(Product, related_name='Review', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)


class Images(ABS):
    products = models.ForeignKey(Product,related_name='images', on_delete=models.CASCADE)
    images_tb = models.ImageField(upload_to = 'img/images ') 
    



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


















































    
                

