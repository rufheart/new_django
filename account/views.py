import email
from webbrowser import get
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
        formData = FormRegister(request.POST)
        if formData.is_valid():
            print('valid')
            if User.objects.filter(username = formData.cleaned_data.get('username')):
                return render(request, 'register.html', {"error":"This username using by other user please choose diffrent username"})
            else:
                formData.save()
                # User.objects.create_user(first_name=formData.cleaned_data.get('first_name'), last_name=formData.cleaned_data.get('last_name'), username=formData.cleaned_data.get('username'), email=formData.cleaned_data.get('email'), password=formData.cleaned_data.get('password'))
                return redirect('login')    
        else:
            context = {
                "forms":FormRegister(request.POST)
            }
            return render(request,"register.html",context)
    context ={
        "forms":FormRegister()
    }

    return render(request=request, template_name='register.html',context=context)