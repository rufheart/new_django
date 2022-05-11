from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from header.models import Product_Detail
from django.utils.text import slugify

@receiver(post_save,sender = Product_Detail)
def create_slug(sender, instance, created, **kwargs):
    old_slug = instance.slug
    new_slug = slugify(f"{instance.desc}-{instance.id}")

    if old_slug != new_slug:
        instance.slug = new_slug
        instance.save()

    if created:
        print('send mail new_user')    