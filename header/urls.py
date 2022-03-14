
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('product/', product, name = 'product'),
    path('about/<int:pk>', about, name='about')
]