import time
from celery import shared_task
from requests import request
from header.models import Detail_Product, Product,Subscriber
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


@shared_task
def exportime():
    time.sleep(10)
    return 'celery run'

@shared_task(bind=True)
def notiftask(*args, **kwargs):
    # print(*args, f'<=================')
    liste=[]
    # for i in args:
    #     for x in i:
    #         liste.append(f"http://127.0.0.1:8000/en/product-detail/{x.slug}")
    #         print(liste)\

    datas = Detail_Product.objects.all().order_by('-id')[:3]
    msj = render_to_string('message.html', context = {'datas':datas})


    send_mail(
        subject='A cool subject',
        message='Bu bir messajdir',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[x for x in Subscriber],
        html_message=msj)  
    return 'celery isledi'          

