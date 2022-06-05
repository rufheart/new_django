import imp
import time
from celery import shared_task



@shared_task
def exportime():
    time.sleep(10)
    return 'celery run'

@shared_task
def notiftask():
    print('product eleave olundu')
    return 'celery run'
