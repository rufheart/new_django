from django.http import Http404
from requests import put, request
from rest_framework.views import APIView, Response
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from header.api import seralize
from header.models import Product,Detail_Product
from header.api.seralize import ProductSerialize, DetailSerialize, CreateSerialize
import json


class DetailApi(APIView):

    def get(self, request, *args, **kwargs):
        category_id = kwargs
        all = Detail_Product.objects.all()
        product=request.GET.get('product')
        if product:
            all=Detail_Product.objects.filter(detail__id=product)

        myJson = DetailSerialize(all, many=True, context= {'request':request})
        return Response(data=myJson.data)




        
        
    def post(self, request, *args, **kwargs):
        data=request.data
        beta=request.data
        data = ProductSerialize(data=data)
        beta = CreateSerialize(data=beta)
        data.is_valid(raise_exception=True)
        data.save()
        beta.is_valid(raise_exception=True)
        beta.save() 
        return Response(data=data.data, status=201)

class FilterApi(APIView):
    def get(self, request, *args, **kwargs):
        all = Detail_Product.objects.filter(id=kwargs['pk']).first()
        if not all:
            raise Http404
        gt = DetailSerialize(all,context={'request':request})
        return Response(data=gt.data)

    def put(self, request, *args, **kwargs):
        print('put isledi================================>>>')
        all = Detail_Product.objects.filter(id=kwargs['pk']).first()
        data=request.data
        data = CreateSerialize(data=data, instance=all)
        data.is_valid(raise_exception=True)
        data.save()
        return Response(data=data.data, status=201)

    def patch(self, request, *args, **kwargs):
        print('put isledi================================>>>')
        all = Detail_Product.objects.filter(id=int(kwargs['pk'])).first()
        data=request.data
        data = CreateSerialize(data=data, instance=all, partial=True)
        data.is_valid(raise_exception=True)
        data.save()
        return Response(data=data.data, status=201)

    def delete(self, request, *args, **kwargs):
        delete1, _ = Detail_Product.objects.filter(id=kwargs['pk']).delete()
        if not delete1:
            raise Http404
        return Response(data={}, status=201)
    

# class ApiCreateView(ListCreateAPIView):
#     queryset = Detail_Product.objects.all()
#     serializer_class=CreateSerialize

#     def get_serializer_class(self):
#         print('def isledi')
#         if self.request.method == 'GET':
#             serializer_class = DetailSerialize
#         return super().get_serializer_class()

class FourApiView(RetrieveUpdateDestroyAPIView):
    queryset = Detail_Product.objects.all()
    serializer_class=DetailSerialize

    def put(self, request, *args, **kwargs):
        if self.request.method == 'PUT':
            seralize_class = CreateSerialize
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if self.request.method == 'PATCH':
            seralize_class = CreateSerialize
        return super().put(request, *args, **kwargs)    

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