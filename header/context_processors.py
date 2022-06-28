from django.shortcuts import render
from header.models import Subscriber
from header.forms import SubscribersForm
from django.shortcuts import redirect, render

def subsc(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subs')
    context = {
        'form':SubscribersForm()
    }        
    return render(request,'susbc.html',context)