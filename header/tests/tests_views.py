from http import client
from django.test import TestCase, Client
from django.urls import reverse_lazy
from rest_framework import status
from header.models import Contact
import json


class TestViews(TestCase):
    def setUp(self) -> None:
        self.views = self.client.get(reverse_lazy('contact'))


    def test2(self):
        self.assertEqual(self.views.status_code, status.HTTP_200_OK)