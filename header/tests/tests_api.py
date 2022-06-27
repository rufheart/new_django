from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import status


class TestApi(TestCase):
    def setUp(self) -> None:
        self.api = self.client.get('http://127.0.0.1:8000/en/api/productapi/4/')

    def test3(self):
        self.assertEqual(self.api.status_code, status.HTTP_200_OK)    