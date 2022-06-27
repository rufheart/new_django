from cProfile import label
from django import forms
from header.models import Cont_Info, Contact, Detail_Product, Review,Product,Add_To_Card,Subscriber
from account.forms import FormRegister
from account.models import User




class FormContact(forms.ModelForm):
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

        def clean(self):
            gmail = self.cleaned_data.get('email')
            if gmail.endswith('@gmail.com') == False:
                raise forms.ValidationError('email sonu duz deyil')
            return super().clean()        


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

class Form_Review(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['value_review', 'quality_review','price_review', 'summary', 'comment' ]

        widgets = {
            'value_review':forms.RadioSelect(attrs={
                'class':'radio'
                }),
            'quality_review':forms.RadioSelect(attrs={
                'class':'radio'
            }),
            'price_review':forms.RadioSelect(attrs={
                "class":"radio"
            }),
            'summary':forms.TextInput(attrs={
                "class":"input-text",
                'id':"summary_field"
            }),
            "comment":forms.Textarea(attrs={
                "id":"review_field"
            })
        }




class Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']

        widgets = {
            'name':forms.TextInput(attrs={
                "class":"form-input",
                "id":"tt"
            })
        }    


class Productdetail_form(forms.ModelForm):
    class Meta:
        model  = Detail_Product
        fields = ['image','desc','new_pr','old_pr',]

        widgets ={
            'desc':forms.Textarea(attrs={
                'class':"form-desc",
                'placeholder':"Description"
            }),
            'new_pr':forms.TextInput(attrs={
                "class":"form-input",
                "placeholder":"New price"
            }),
            "old_pr":forms.TextInput(attrs={
                "class":"form-input",
                "placeholder":"Old price"
            })
        }
        label={
            'desc':"Description"
        }

class Add_CardForm(forms.ModelForm):
    class Meta:
        model = Add_To_Card
        fields = ['add_product','add_usr']

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['subscribers_emails']        