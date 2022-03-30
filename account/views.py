from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request,username=name,password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request,'login.html', )  

    return render(request,'login.html', {'error':'User or password incorrect'} )
