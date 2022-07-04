from django.urls import path
from account.api.views import *

urlpatterns = [
    path('registerapi/',DetailApi.as_view(), name='registerapi'),
]