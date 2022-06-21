from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from requests import request
from header.models import Detail_Product,Product
from django.utils.text import slugify
# from header.views import notif
from header.task import notiftask
# from rufat.celery import notiftask

count=0
liste = []

@receiver(post_save, sender = Detail_Product)
def create_slug(sender, instance, created, **kwargs):
    old_slug = instance.slug
    new_slug = slugify(f"{instance.desc}-{instance.id}")
    
    if old_slug != new_slug:
        instance.slug = new_slug
        instance.save()

    if created:
        notiftask.delay()
    #     global count
    #     count+=1
    #     global liste
        
        # liste.append(instance)
        # if count==1:
        #     notiftask.delay(liste)

        # if count == 1:
        #     count=0
        #     liste=[]
           
