
from django import forms
# from django.contrib.auth.models import User
from account.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class FormLogin(AuthenticationForm):
    pass


# class FormLogin(forms.ModelForm):

#     submit = forms.CharField(widget=forms.TextInput(attrs={"class":"button login","id":"send2","value":"Login","type":"submit"}))

#     class Meta:
#         model = User
#         fields = "__all__"

#         widgets = {
#             "username":forms.TextInput(attrs={"class":"input-text", "id":"uname", "placeholder":"Username"}),
#             "password":forms.PasswordInput(attrs={"class":"input-text", "id":"pass", "placeholder":"Password"})
#         }

#         labels = {
#             "username":"Username",
#             "password":"Password"
#         }

class FormRegister(UserCreationForm):
    pass
    




    # class Meta:
    #     model = User
    #     fields = ('image','username', 'first_name', 'last_name', 'email', 'password')

    #     widgets = {
    #         "username":forms.TextInput(attrs={"class":"input-text","id":"pass2", "placeholder":"Username"}),
    #         "first_name":forms.TextInput(attrs={"class":"input-text","id":"name", "placeholder":"First Name"}),
    #         "last_name":forms.TextInput(attrs={"class":"input-text", "id":"surname", "placeholder":"Last Name"}),
    #         "email":forms.EmailInput(attrs={"class":"input-text","id":"email", "placeholder":"Email"}),
    #         "password":forms.PasswordInput(attrs={"class":"input-text","id":"pass", "placeholder":"Password","type":"password"})
    #     }
        
    # def save(self, *args, **kwargs):
        
    #     User.objects.create_user(first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), username=self.cleaned_data.get('username'), email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
    #     # User.first_name = self.cleaned_data.get('first_name')
        # User.last_name = self.cleaned_data.get('last_name')
        # User.email = self.cleaned_data.get('email')
    



        


    def clean(self):
        gmail = self.cleaned_data.get('email')
        if gmail.endswith('@gmail.com') == False:
            raise forms.ValidationError('Bu yalniz gmaillla qeydiyyat mumkundur')

        return super().clean()


class FormUpdate_Profile(forms.ModelForm):

    # username=forms.CharField(),
    # first_name=forms.CharField(),
    # last_name=forms.CharField(),
    # email=forms.EmailField(),
    # password=forms.CharField(widget={})
    

    class Meta:
        model=User
        fields = ('image','username','first_name','last_name','email','password')

        widgets = {
            'password': forms.PasswordInput(attrs={
                'class':'password'
            }),
            'username':forms.TextInput(attrs={
                'class':'username',
                
            }),
            'first_name':forms.TextInput(attrs={
                'class':'First Name'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'last_name',
                
            }),
            'email':forms.EmailInput(attrs={
                'class':'email',
              
            })
        }
    
    
    def save(self, userId, commit=True):

        form = self.cleaned_data
        user = User.objects.get(id = userId)
        user.username = form.get('username')
        user.image = form.get('image')
        user.first_name = form.get('first_name')
        user.last_name = form.get('last_name')
        user.email = form.get('email')
        user.set_password(form.get('password'))
        user.save()

        return user        