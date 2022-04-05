from django import forms
from django.contrib.auth.models import User

class FormLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

        widgets = {
            "username":forms.TextInput(attrs={"class":"input-text", "id":"uname", "placeholder":"Username"}),
            "password":forms.PasswordInput(attrs={"class":"input-text", "id":"pass", "placeholder":"Password"})
        }

        labels = {
            "username":"Username",
            "password":"Password"
        }

class FormRegister(forms.ModelForm):

    submit = forms.CharField(widget=forms.TextInput(attrs={"type":"submit", "class":"button login","id":"send2", "value":"Submit"}))


    class Meta:
        model = User
        fields = "__all__"

        widgets = {
            "first_name":forms.TextInput(attrs={"class":"input-text","id":"name", "placeholder":"First Name" }),
            "last_name":forms.TextInput(attrs={"class":"input-text", "id":"surname", "placeholder":"Last Name"}),
            "email":forms.TextInput(attrs={"class":"input-text","id":"email", "placeholder":"Email"}),
            "password":forms.TextInput(attrs={"class":"input-text","id":"pass", "placeholder":"Password"}),
            "username":forms.TextInput(attrs={"class":"input-text","id":"pass2", "placeholder":"Username"})
        }

        labels = {
            "first_name":"First Name",
            "last_name":"Last Name",
            "email":"Email",
            "password":"Password",
            "username":"Username"
        }
