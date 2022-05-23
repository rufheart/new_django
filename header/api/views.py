# from django.http import HttpResponse
from multiprocessing import context
from rest_framework.views import APIView, Response
from header.models import Product
from header.api.seralize import ProductSerialize
import json


class ProductApi(APIView):

    def get(self, request, *args, **kwargs):
        all = Product.objects.all()
        myJson = ProductSerialize(all, many=True, context= {'request':request})
        return Response(data=myJson.data)





# class ProductApi(APIView):

#     def get(self, request, *args, **kwargs):
#         data1 = Detail_Product.objects.all()
#         myJson = []
#         for i in data1:
#             myJson.append({'id':i.id, 'desc':i.desc})
#         return Response(data=myJson)    






# def productApi(request):
#     data = Detail_Product.objects.all()
#     myJson = []
#     for i in data:
#         myJson.append({'id':i.id,'desc':'i.desc'})
#     return HttpResponse(json.dumps(myJson))