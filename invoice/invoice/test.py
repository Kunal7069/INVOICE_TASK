from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from myapp.models import *  
from .serializers import *

class GetInvoiceFromURLAPIViewTest(TestCase):
    def setUp(self):
        self.invoice1 = Invoice.objects.create(date='2024-01-16', customer_name='Customer1')
        self.invoice2 = Invoice.objects.create(date='2024-01-17', customer_name='Customer2')

    def test_get_invoices(self):
        client = APIClient()
        self.url = 'invoices'
        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = InvoiceSerializer(Invoice.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)

class CreateInvoiceDetailFromURLAPIViewTest(TestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create()
        self.test_data = {
            'description': 'Test Item',
            'quantity': 2,
            'unit_price': 10.0,
            'price': 20.0,
        }
        self.client = APIClient()

    def test_create_invoice_detail_success(self):
        url = reverse('createinvoicesdetail', args=[self.invoice.id])
        response = self.client.get(url, data=self.test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 1)
        invoice_detail = InvoiceDetail.objects.first()
        self.assertEqual(invoice_detail.invoice, self.invoice)
        self.assertEqual(invoice_detail.description, self.test_data['description'])
        self.assertEqual(invoice_detail.quantity, self.test_data['quantity'])
        self.assertEqual(invoice_detail.unit_price, self.test_data['unit_price'])
        self.assertEqual(invoice_detail.price, self.test_data['price'])

    def test_create_invoice_detail_duplicate(self):
        InvoiceDetail.objects.create(invoice=self.invoice, **self.test_data)
        url = reverse('createinvoicesdetail', args=[self.invoice.id])
        response = self.client.get(url, data=self.test_data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(InvoiceDetail.objects.count(), 1)