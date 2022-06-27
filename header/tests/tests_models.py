from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import status
from header.models import Contact

class TestContact(TestCase):
    def setUp(self) -> None:
        self.models = {
            'name':'rufat',
            'email':'rufat@gmail.com',
            'company':'MEK',
            'tel':'0705856719',
            'address':'Baku',
            'comment':'REY'
        }

    def test(self):
        result =  Contact.objects.create(**self.models)
        self.assertEqual((result.name,result.email,result.company,result.tel,result.address,result.comment),(self.models.get('name'),self.models.get('email'),self.models.get('company'),self.models.get('tel'),self.models.get('address'),self.models.get('comment')))