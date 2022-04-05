from django import forms
from header.models import Cont_Info, Contact

class FormContact(forms.ModelForm):
    submit = forms.CharField(widget=forms.TextInput(attrs={
        'type':'submit',
        'title':'Submit',
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


class Form_Cont_Info(forms.ModelForm):
    submit = forms.TextInput(attrs={"type":"submit","class":"button"})
    
    class Meta:
        model = Cont_Info
        fields = '__all__'

        widgets = {
            'fname':forms.TextInput(attrs={"class":"input-text required-entry","id":"firstname","placeholder":"First Name"}),
            'lname':forms.TextInput(attrs={"class":"input-text required-entry","id":"lastname","placeholder":"Last Name"}),
            'company':forms.TextInput(attrs={"class":"input-text","id":"company","placholder":"Company","placeholder":"Company"}),
            'tel':forms.TextInput(attrs={"class":"input-text   required-entry","id":"telephone","placeholder":"Telephone"}),
            'fax':forms.TextInput(attrs={"class":"input-text ","id":"fax","placeholder":"Fax"}),
            's_address':forms.TextInput(attrs={"class":"input-text  required-entry","id":"street_1","placeholder":"Street_1"}),
            's_2address':forms.TextInput(attrs={"class":"input-text ", "id":"street_2"}),
            'city':forms.TextInput(attrs={"class":"input-text  required-entry","placeholder":"City"}),
            'state':forms.Select(attrs={"class":"validate-select required-entry","id":"region_id","placholder":"Please select region, state or province"}),
            'zip':forms.TextInput(attrs={"class":"input-text validate-zip-international  required-entry", "id":"zip","placeholder":"Zip"}),
            'country':forms.Select(attrs={"class":"validate-select","id":"country"}),
            'bil_addr':forms.CheckboxInput(attrs={"class":"checkbox","id":"primary_billing"}),
            'ship_addr':forms.CheckboxInput(attrs={"class":"checkbox","id":"primary_shipping"})
        }
        labels = {
            "fname":"First Name",
            "lname":"Last Name",
            "company":"Company",
            "tel":"Telephone",
            "fax":"Fax",
            "s_address":"Street Address",
            "city":"City",
            "state":"State/Province",
            "zip":"Zip/Postal Code",
            "country":"Country",
            "bil_addr":"Use as my default billing address",
            "ship_addr":"Use as my default shipping address"
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




