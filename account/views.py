
from distutils import errors
from re import template
from webbrowser import get
from django import dispatch
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
# from django.contrib.auth.models import User
# from account.models import User
from account.forms import FormLogin, FormRegister, FormUpdate_Profile
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
import json


User = get_user_model()



class Login_User(LoginView):
    template_name = 'login.html'
    succes_url = reverse_lazy('profile')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)

# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect('index')
        
#     if request.method == 'POST':
#         username= request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username = username, password = password)
#         if user:
#             login(request, user)
#             return redirect('index')
#         else:
#             return render(request,'login.html', )  
#     context = {
#         'error':'User or password incorrect',
#         'forms':FormLogin()
#         } 
#     return render(request,'login.html', context)


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


class Logout_User(LogoutView):
    pass

# def logout_user(request):
#     logout(request)
#     return redirect('login')

class UserCreate(CreateView):
    template_name = 'register.html'
    form_class = FormRegister
    success_url = reverse_lazy('login')

    


# def register_user(request):
#     if request.method == "POST":
#         formData = FormRegister(request.POST, request.FILES)
#         print(formData)
#         if formData.is_valid():
#             if User.objects.filter(username = formData.cleaned_data.get('username')):
#                 return render(request, 'register.html', {"error":"This username using by other user please choose diffrent username"})
#             else:
#                 a=formData.save()
#                 a.set_password(a.password)
#                 a.save()

#                 # User.objects.create_user(first_name=formData.cleaned_data.get('first_name'), last_name=formData.cleaned_data.get('last_name'), username=formData.cleaned_data.get('username'), email=formData.cleaned_data.get('email'), password=formData.cleaned_data.get('password'))
#                 return redirect('login')    
#         else:
#             context = {
#                 "forms":FormRegister(request.POST)
#             }
#             return render(request,"register.html",context)
#     context ={
#         "forms":FormRegister()
#     }

#     return render(request=request, template_name='register.html',context=context)


def profile(request):
    args = {}
    user = User
    if request.method == 'POST':
        form = FormUpdate_Profile(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(request.user.id)

    else:
        form = FormUpdate_Profile()
    
    form.initial['username'] = request.user.username
    form.initial['first_name'] = request.user.first_name
    form.initial['last_name'] = request.user.last_name
    form.initial['email'] = request.user.email
    form.initial['password'] = request.user.password

    user = User.objects.get(id = request.user.id)
    user = dict(username = user.username, password = user.password)

    args = {
        'form':form,
        'user1':User.objects.get(id=request.user.id),
        'user': json.dumps(user)
        }

    return render(request, 'profile.html', args)