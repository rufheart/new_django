
from crypt import methods
from django.shortcuts import redirect, render
from django.http import Http404, HttpRequest, HttpResponse
from header.forms import FormContact,Form_Cont_Info, Form_Review
from header.models import Contact, Product, Review

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):    
    return render(request=request, template_name='blog.html')    

def contact(request):
    if request.method == 'POST':
        formsData=FormContact(request.POST)
        print(formsData)
        if formsData.is_valid():
            formsData.save()
    
    context = {
        'forms':FormContact()
        }        
    return render(request, 'contact_us.html',context)    

def product(request):
    context = {
        'models':Product.objects.all()
    }
    print(context.get('models'))
    return render(request, 'product-list.html', context)

def about(request, slug):
    context = {
        'about':Product.objects.get(slug = slug),   
        'forms': Form_Review()
    }
    
    return render(request, 'product-detail.html', context)

def cont_info(request):
    if request.method == 'POST':
        formData = Form_Cont_Info(request.POST)
        print(Form_Cont_Info())
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

def review(request):
    if request.method == "POST":
        formData = Form_Review(request.POST)
        if formData.is_valid():
            formData.save()
        return redirect('index')    
    return render(request, 'review.html')    