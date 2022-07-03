from functools import partial
from multiprocessing import context
from unicodedata import category
from django.http import Http404
from requests import put, request
from rest_framework.views import APIView, Response
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


