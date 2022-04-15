
from django import forms
# from django.contrib.auth.models import User
from account.models import User

class FormLogin(forms.ModelForm):

    submit = forms.CharField(widget=forms.TextInput(attrs={"class":"button login","id":"send2","value":"Login","type":"submit"}))

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

    # submit = forms.CharField(widget=forms.TextInput(attrs={"type":"submit", "class":"button login","id":"send2", "value":"Register"}))

    class Meta:
        model = User
        fields = ('image', 'username', 'first_name', 'last_name', 'email', 'password')

        widgets = {
            "username":forms.TextInput(attrs={"class":"input-text","id":"pass2", "placeholder":"Username"}),
            "first_name":forms.TextInput(attrs={"class":"input-text","id":"name", "placeholder":"First Name"}),
            "last_name":forms.TextInput(attrs={"class":"input-text", "id":"surname", "placeholder":"Last Name"}),
            "email":forms.EmailInput(attrs={"class":"input-text","id":"email", "placeholder":"Email"}),
            "password":forms.PasswordInput(attrs={"class":"input-text","id":"pass", "placeholder":"Password","type":"password"})
        }
        
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
