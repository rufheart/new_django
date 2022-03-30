from django.urls import path
from account.views import *
from django.conf import settings 

urlpatterns = [
    path('login/', login_user, name='login'),
]