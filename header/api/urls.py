from django.urls import path
from header.api.views import *


urlpatterns = [
    path('productapi/',ProductApi.as_view())
]