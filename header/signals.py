from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from requests import request
from header.models import Detail_Product,Product
from django.utils.text import slugify
from header.views import notif

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
        global count
        count+=1
        print(count)
        a=Detail_Product.objects.get(id=instance.id)
        global liste
        liste.append(a)
        if count==3:
            notif(liste)
            print('3 produt elave olunub ==============>')

        if count == 3:
            count=0
            liste=[]
           
