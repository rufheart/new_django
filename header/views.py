
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
    print(context.get('models'))
    return render(request, 'product-list.html', context)

def about(request, pk):
    context = {
        'abouts':Product.objects.filter(abs_ptr_id = pk)[0]
    }
    print(context.get('abouts'))
    return render(request, 'product-detail.html', context)
