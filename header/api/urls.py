from django.urls import path
from header.api.views import *

 
urlpatterns = [
    path('productapi/',DetailApi.as_view(), name='test')
]