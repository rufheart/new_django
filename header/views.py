from dataclasses import field
from multiprocessing import get_context
from re import template
from unicodedata import category
from venv import create
from django import views
from django.forms import SlugField, ValidationError
from django.shortcuts import redirect, render
from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse_lazy
from pyparsing import ParseSyntaxException
from requests import request
from header.forms import Add_CardForm, Form_Review, Productdetail_form, Product_Form,FormContact,Form_Cont_Info,SubscribersForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View, DeleteView
import json
from header.models import Category, Product, Detail_Product, Add_To_Card, Subscriber
from header.task import exportime


class IndexView(TemplateView):
    template_name = 'index.html'


   
class BlogView(TemplateView):
    template_name = 'blog.html'

class ContactView(CreateView):
    form_class=FormContact
    template_name = 'contact_us.html'
    success_url = reverse_lazy('contact')

 

class Product_View(ListView):
    model=Product
    fields =['name']
    template_name = 'product-list.html'
    context_object_name = 'models'


    def get_context_data(self, **kwargs):
        self.category_id = self.kwargs

        context = super().get_context_data(**kwargs)
        context['categ'] = Category.objects.all

        if self.category_id != {}:
            data = Product.objects.filter(category_pro = self.category_id['id'])  
            context = super().get_context_data(**kwargs)
            context['categ'] = Category.objects.all
            context['models'] = data
        
        return context



  
class ProductDetail_View(DetailView):
    model = Detail_Product
    template_name = 'product-detail.html'
    context_object_name = 'product_detail'

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['forms'] = Form_Review
        return data
    

class ContInfo_View(CreateView):
    form_class = Form_Cont_Info
    template_name = 'contact_information.html'
    success_url = reverse_lazy('cont_info')
    
def cont_info(request):
    if request.method == 'POST':
        formData = Form_Cont_Info(request.POST)
        if formData.is_valid():
            formData.save()
        else:
            context={
                "contc":formData
            }
            return render(request,'contact_information.html', context) 

    context = {
        'contc':Form_Cont_Info()
    }
    return render(request,'contact_information.html',context)

def prod(request):
    return render(request, 'prodc.html')




class ReviewCreate_View(View):
    form_class = Form_Review
    template_name = 'test.html'
    context_object_name = 'forms'
    success_url = reverse_lazy('index')


    
    def post(self, request, pk, slug):
        form = Form_Review(request.POST)
        form.instance.user_pro = self.request.user
        form.instance.product_review = Product.objects.get(id=pk)
        form.save()
        return redirect(reverse_lazy('productdetail', kwargs={'slug':slug}))
    



class ProductCreate_View(TemplateView):
    template_name = 'prodc.html'
    

    def post(self, request):
        name = request.POST.get('name')
        user = request.user
        a = Product.objects.create(user=user,name=name)
        image=request.FILES.get('image')
        desc = request.POST.get('desc')
        new_pr = request.POST.get('new_pr')
        old_pr = request.POST.get('old_pr')
        Detail_Product.objects.create(detail=a, image=image, desc=desc,new_pr=new_pr,old_pr=old_pr)
        return redirect('productcreate')
        
        
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form1'] = Product_Form
        data['form2'] = Productdetail_form
        return data
     



class Add_To_Card_View(View):
    template_name = 'product-detail.html'
    form_class = Add_CardForm
    
    def get(self, request, pk, slug):
        form = Add_CardForm()
        a= request.user
        b= Detail_Product.objects.get(id=pk)
        Add_To_Card.objects.create(add_product=b, add_usr=a)
        return redirect(reverse_lazy('productdetail', kwargs={'slug':slug}))


def export(request):
    exportime.delay()
    return redirect('/')

# def notif(request):
#     notiftask.delay()
#     notiftask(request)
#     return HttpRequest

def get_view(request):
    if request.method == 'POST':
        data = request.POST.get('email')
        b=Subscriber(subscribers_emails=data)
        b.save()
        return redirect('index')
    
class DeleteFromCard(DeleteView):
    model=Add_To_Card
    template_name = 'nav.html'

    def get(self, request,pk, slug):
        data = Add_To_Card.objects.get(add_product=pk)
        data.delete()
        return redirect(reverse_lazy('productdetail', kwargs={'slug':slug}))
