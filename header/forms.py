from django import forms
from header.models import Contact

class FormContact(forms.ModelForm):
    submit = forms.CharField(widget=forms.TextInput(attrs={
        'type':'submit',
        'title':'ubmit',
        'class':"button submit"
    }))
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class':'input-text','title':'First Name','id':'billing:firstname','placeholder':'Name'}),
            'email': forms.EmailInput(attrs={'class':'input-text','title':'Last Name','id':'billing:lastname','placeholder':'Email' }),
            'company':forms.TextInput(attrs={'class':'input-text','title':'Company','id':'billing:company','placeholder':'Company' }),
            'tel':forms.TextInput(attrs={'class':'input-text','title':'Email Address','id':'billing:email', 'placeholder':'Telephone' }),
            'address':forms.TextInput(attrs={'class':'input-text','title':'Street Address','placeholder':'Address'}),
            'comment':forms.Textarea(attrs={'class':'input-text','title':'Comment','id':'comment','placeholder':'Comment' })
        }


# class FormContact(forms.Form):
#     name = forms.CharField(label='First Name', max_length=50,min_length=3 ,widget=forms.TextInput(attrs={
#         'class':'input-text',
#         'title':'First Name',
#         'id':'billing:firstname'
#     }))

#     email = forms.EmailField(label='Email Address', max_length=50, min_length=6 ,widget=forms.TextInput(attrs={
#         'class':'input-text',
#         'title':'Last Name',
#         'id':'billing:lastname' 
#     }))

#     company = forms.CharField(label='Company', max_length=50, min_length=3, widget=forms.TextInput(attrs={
#         'class':'input-text',
#         'title':'Company',
#         'id':'billing:company' 
#     }))

#     tele = forms.CharField(label='Telephone', max_length=13, min_length=13, widget=forms.TextInput(attrs={
#         'class':'input-text',
#         'title':'Email Address',
#         'id':'billing:email' 
#     }))

#     address = forms.CharField(label='Address', max_length=40, min_length=6, widget=forms.TextInput(attrs={
#         'class':'input-text',
#         'title':'Street Address',       
#     }))

#     comment = forms.CharField(label='Comment', widget=forms.Textarea(attrs={
#         'class':'input-text',
#         'title':'Comment',
#         'id':'comment'        
#     }))




