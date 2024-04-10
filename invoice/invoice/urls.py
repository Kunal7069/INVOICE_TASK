"""
URL configuration for invoice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
# router = DefaultRouter()
# router.register(r'getinvoice', GetInvoiceFromURLAPIView.get_queryset() , basename='invoice')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoices', GetInvoiceFromURLAPIView.as_view(), name='invoice-list'),
    path('createinvoices/<str:date>/<str:customer_name>/', CreateInvoiceFromURLAPIView.as_view(), name='invoice-create'),
    path('createinvoicesdetail/<str:invoice_id>/<str:description>/<str:quantity>/<str:unit_price>/<str:price>/', CreateInvoiceDetailFromURLAPIView.as_view(), name='invoicedetail-create'),
]
