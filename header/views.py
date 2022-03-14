
from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse
from header.forms import FormContact
from header.models import Contact, Product

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):    
    return render(request=request, template_name='blog.html')    

def contact(request):
    if request.method == 'POST':
        short = request.POST
        formsData=FormContact(short)
        if formsData.is_valid():
            contact = Contact()

    context = {
        'forms':FormContact()
    }        
    return render(request, 'contact_us.html',context)    

def product(request):
    context = {
        'models':Product.objects.all()
    }
    return render(request, 'product-list.html', context)

def about(request, pk):
    context = {
        'about':Product.objects.get(id = pk)
    }
    return render(request, 'product-details.html', context=context)
