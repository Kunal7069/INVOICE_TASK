from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from myapp.models import *
from .serializers import InvoiceSerializer,InvoiceDetailSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
class CreateInvoiceFromURLAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        date = self.kwargs.get('date')
        customer_name = self.kwargs.get('customer_name')
        en=Invoice(date=date,customer_name=customer_name)
        queryset= Invoice.objects.filter(date=date,customer_name=customer_name)
        print(len(queryset))
        if len(queryset)==0: 
            en.save()
            return Response(status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_204_NO_CONTENT)
        
class CreateInvoiceDetailFromURLAPIView(ListAPIView):
    def get(self, request,invoice_id, *args, **kwargs):
        invoice = get_object_or_404(Invoice, pk=invoice_id)
        description = self.kwargs.get('description')
        quantity = self.kwargs.get('quantity')
        unit_price = self.kwargs.get('unit_price')
        price = self.kwargs.get('price')
        en=InvoiceDetail(invoice=invoice,description=description,quantity=quantity,unit_price=unit_price,price=price)
        queryset= InvoiceDetail.objects.filter(invoice=invoice,description=description,quantity=quantity,unit_price=unit_price,price=price)
        print(len(queryset))
        if len(queryset)==0: 
            en.save()
            return Response(status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_204_NO_CONTENT)


class GetInvoiceFromURLAPIView(ListAPIView):
    serializer_class = InvoiceSerializer
    def get_queryset(self):
        return Invoice.objects.all()