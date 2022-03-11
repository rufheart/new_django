from django.shortcuts import render
from django.http import HttpResponse
from header.forms import FormContact
from header.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):    
    return render(request=request, template_name='blog.html',context=context)    

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


