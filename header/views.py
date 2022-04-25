from calendar import c
from dataclasses import field
from re import template
from urllib import request
from xml.parsers.expat import model
from django.forms import SlugField, ValidationError
from django.shortcuts import redirect, render
from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse_lazy
from header.forms import FormContact,Form_Cont_Info, Form_Review, Form_Product
from header.models import Contact, Product, Review, Add_To_Card
from django.views.generic import TemplateView, CreateView, ListView


class IndexView(TemplateView):
    template_name = 'index.html'

# def index(request):
#     return render(request, 'index.html')

# def blog(request):    
#     return render(request=request, template_name='blog.html')    
class BlogView(TemplateView):
    template_name = 'blog.html'

class ContactView(CreateView):
    form_class=FormContact
    template_name = 'contact_us.html'
    success_url = reverse_lazy('contact')



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
class Product_List(ListView):
    model=Product
    fields ='__all__'
    template_name = 'product-list.html'
    context_object_name = 'models'

    


# def product(request):
#     context = {
#         'models':Product.objects.all()
#     }
#     return render(request, 'product-list.html', context)

def about(request, slug):
    context = {
        'about':Product.objects.get(slug = slug),   
        'forms': Form_Review()
    }
    
    return render(request, 'product-detail.html', context)

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

# def prod(request):
#     return render(request, 'prodc.html')


class Review_Create(CreateView):
    form_class = Form_Review
    print('1')
    def form_valid(self, form):
        form.instance.user_pro = self.request.user
        form.instance.product_review=Product.objects.get(id=1)
        return super().form_valid(form)
    



# def review(request):
#     if request.method == "POST":
#         formData = Form_Review(request.POST)
#         if formData.is_valid():
#             formData.save()
#         return redirect('index')    
#     return render(request, 'review.html')    

def product_det(request):
    if request.method =='POST':
        formData=Form_Product(request.POST, request.FILES)
        if formData.is_valid():
            formData.save()
            a=Product.objects.get(user_id=None)
            a.user_id=request.user.id
            a.save()
        else:
            print(formData.errors)
            
            context={ 
                'forms':Form_Product(),
                }
            return render(request, 'prodc.html', context)  
    context={
        'forms':Form_Product(),
    }          
    return render(request, 'prodc.html', context)        

def add_to_card(request, pk, slug):
    user = request.user
    Add_To_Card.objects.create(add_usr=user, add_product=Product.objects.get(id=pk))
    return redirect(reverse_lazy('about', kwargs={'slug':slug}))