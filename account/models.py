from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to = 'img/use')