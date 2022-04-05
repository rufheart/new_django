import email
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.forms import FormLogin, FormRegister

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request,'login.html', )  
    context = {
        'error':'User or password incorrect',
        'forms':FormLogin()
        } 
    return render(request,'login.html', context)


# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect('index')
        
#     if request.method == 'POST':
#         uname = request.POST.get('uname')
#         password = request.POST.get('password')
#         user = authenticate(request, username = uname, password = password)
#         if user:
#             login(request, user)
#             return redirect('index')
#         else:
#             return render(request,'login.html', )  

#     return render(request,'login.html', {'error':'User or password incorrect'} )    

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        name=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if User.objects.filter(username = uname):
            return render(request, 'register.html', {"error":"This username using by other user please choose diffrent username"})
        else:
            User.objects.create_user(first_name=name, last_name=lname, username=uname, email=email, password=password)
            return redirect('login')    

    context ={
        "forms":FormRegister()
    }

    return render(request=request, template_name='register.html',context=context)