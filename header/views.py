from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request=request, template_name='blog.html')    

def contact(request):
    return render(request, 'contact_us.html')    


