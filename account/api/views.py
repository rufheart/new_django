from django.http import Http404
from requests import put, request
from rest_framework.views import APIView, Response
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from account.api.serialize import *
from account.models import User
import json

# class RegisterWithApi(CreateAPIView):
#     print('registerisledi')
#     def get(self, request, *args, **kwargs):
#         data = request.GET.get('register')
#         return Response(data=data)

class DetailApi(APIView):

    def get(self, request, *args, **kwargs):
        category_id = kwargs
        all = User.objects.all()
        product=request.GET.get('register')
        if product:
            all=User.objects.filter(detail__id=product)

        myJson = UserSerialize(all, many=True, context= {'request':request})
        return Response(data=myJson.data)

    def post(self, request, *args, **kwargs):
        print(request.data,'++++++++++++++++')
        data = request.data
        data = UserSerialize(data=data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response(request.data)