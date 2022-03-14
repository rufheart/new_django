from calendar import c
from distutils.command.upload import upload
import email
from email.mime import image
from pyexpat import model
from django.db import models

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

class Product(ABS):
    name=models.CharField(max_length=35)
    image = models.ImageField(upload_to = 'img/product/')
    desc = models.TextField()
    new_pr=models.CharField(max_length=10)
    old_pr=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class About(ABS):
    name = models.CharField(max_length=40)



















































    
                

