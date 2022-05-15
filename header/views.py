from django import views
from django.forms import SlugField, ValidationError
from django.shortcuts import redirect, render
from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse_lazy
from requests import request
from header.forms import Add_CardForm, Form_Review, Productdetail_form, Product_Form
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View
import json
from header.models import Category, Product, Detail_Product, Add_To_Card
# from multi_form_view import MultiModelFormView


class IndexView(TemplateView):
    template_name = 'index.html'

# https://www.tutorialspoint.com/django-handling-multiple-forms-in-single-view                   django multimodelformview link



# def blog(request):    
#     return render(request=request, template_name='blog.html')    
# class BlogView(TemplateView):
#     template_name = 'blog.html'

# class ContactView(CreateView):
#     form_class=FormContact
#     template_name = 'contact_us.html'
#     success_url = reverse_lazy('contact')



# def contact(request):
#     if request.method == 'POST':
#         formsData=FormContact(request.POST)
#         print(formsData)
#         if formsData.is_valid():
#             formsData.save()
    
#     context = {
#         'forms':FormContact()
#         }        
#     return render(request, 'contact_us.html',context)    

class Product_View(ListView):
    model=Product
    fields =['name']
    template_name = 'product-list.html'
    context_object_name = 'models'


    

class ProductDetail_View(DetailView):
    model = Detail_Product
    template_name = 'product-detail.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['forms'] = Form_Review
        return data




# def cont_info(request):
#     if request.method == 'POST':
#         formData = Form_Cont_Info(request.POST)
#         if formData.is_valid():
#             formData.save()
#         else:
#             context={
#                 "contc":formData
#             }
#             return render(request,'contact_information.html', context) 

#     context = {
#         'contc':Form_Cont_Info()
#     }
#     return render(request,'contact_information.html',context)

# def prod(request):
#     return render(request, 'prodc.html')




class ReviewCreate_View(View):
    form_class = Form_Review
    template_name = 'test.html'
    context_object_name = 'forms'
    success_url = reverse_lazy('index')

    # def form_valid(self, form):      
    #     form.instance.user_pro = self.request.user
    #     # form.instance.product_review = Product.objects.get(id =  1)
    #     form.instance.product_review  = Product.objects.get(id =  self.kwargs['pk'])

    #     return super().form_valid(form)

    # def dispatch(self, request: HttpRequest, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    # def get(self, request: HttpRequest, *args, **kwargs):
    #     data =  super().get(request, *args, **kwargs)
    #     print('==============>', data)
    
    def post(self, request, pk, slug):
        form = Form_Review(request.POST)
        form.instance.user_pro = self.request.user
        form.instance.product_review = Product.objects.get(id=pk)
        form.save()
        return redirect(reverse_lazy('productdetail', kwargs={'slug':slug}))
    

    # def get(self, request):
    #     print("get isledi ============> ")
    #     return render(request=request, template_name='test.html')



# def review(request, pk):
#     form = Form_Review(request.POST)
#     if form.is_valid:
#         form.instance.user_pro = request.user
#         form.instance.product_review = Product.objects.get(id = pk)
#         form.save()

#     return HttpResponse('asasa')










class ProductCreate_View(CreateView):
    form_class={
        'prod':Product_Form,
        'detail':Detail_Product,
    }
    template_name = 'prodc.html'
    def get_success_url(self):
        return redirect('productcreate')

    def form_valid(self, forms):
        prod = forms['prodc'].save(commit=False)
        detail = forms['detail'].save(commit=False)
        return super(ProductCreate_View,self).form_valid(forms)








def create(request):
    context = {
        'form': Product_Form(),
        'form1': Productdetail_form()
    }

    return render(request, 'prodc.html', context=context)

# def product_create(request):
#     if request.method =='POST':
#         formData=CreateProduct_Form(request.POST, request.FILES)
#         if formData.is_valid():
#             formData.instance.user=request.user
#             formData.save()
#         else:
#             print(formData.errors)
            
#             context={ 
#                 'forms':CreateProduct_Form(),
#                 }
#             return render(request, 'prodc.html', context)  
#     context={
#         'forms':,
#     }          
#     return render(request, 'prodc.html', context)        



class Add_To_Card_View(View):
    template_name = 'product-detail.html'
    form_class = Add_CardForm
    
    def get(self, request, pk, slug):
        form = Add_CardForm()
        form.instance.add_usr = request.user
        form.instance.add_product = Product.objects.get(id=pk)
        form.save()
        return redirect(reverse_lazy('productdetail', kwargs={'slug':slug}))

# def add_to_card(request, pk, slug):
#     user = request.user
#     print('add_card_isledi','=========================================>>>')
#     Add_To_Card.objects.create(add_usr=user, add_product=Product.objects.get(id=pk))
#     return redirect(reverse_lazy('productdetail', kwargs={'slug':slug}))

