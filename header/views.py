
from crypt import methods
from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse
from header.forms import FormContact,Form_Cont_Info
from header.models import Contact, Product

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

def about(request, pk):
    context = {
        'abouts':Product.objects.filter(abs_ptr_id = pk)
    }
    print(context.get('abouts'))
    return render(request, 'product-detail.html', context)

def cont_info(request):
    if request.method == 'POST':
        formData = Form_Cont_Info(request.POST)
        print(formData)
        if formData.is_valid():
            print('if isledi =====>')
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
