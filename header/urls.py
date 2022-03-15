
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('product/', product, name = 'product'),
    path('about/<int:pk>', about, name='about')
] + static(settings.MEDIA_URL, doument_root = settings.MEDIA_ROOT)