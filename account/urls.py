from unicodedata import name
from django.urls import path
from account.views import *
from django.conf import settings 

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logut/', logout_user, name='logout'),
    path('register/', UserCreate.as_view(), name='register',)
]