# from django.http import HttpResponse
from multiprocessing import context
from rest_framework.views import APIView, Response
from header.models import Product,Detail_Product
from header.api.seralize import ProductSerialize, DetailSerialize, CreateSerialize
import json


class DetailApi(APIView):

    def get(self, request, *args, **kwargs):
        all = Detail_Product.objects.all()
        myJson = DetailSerialize(all, many=True, context= {'request':request})
        return Response(data=myJson.data)
    
    def post(self, request, *args, **kwargs):
        data=request.data
        data = ProductSerialize(data=data)
        data.is_valid(raise_exception=True)
        data.save()
        print(data.id)
        return Response(data=data.data, status=201)

    # def post(self, request, *args, **kwargs):
    #     data=request.data
    #     data = CreateSerialize(data=data)
    #     data.instance.detail=P
    #     data.is_valid(raise_exception=True)
    #     data.save()
    #     return Response(data=data.data, status=201)
        



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