from unicodedata import name
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('product/', product, name = 'product'),
    path('about/<slug:slug>', about, name='about'),
    path('cont_info/', cont_info, name = 'cont_info'),
    path('prodc/', prod, name='prod'),
    path('review/<int:pk>/', review, name='review'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)