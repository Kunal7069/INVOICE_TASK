from django.contrib import admin
from .models import *
# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display=('date','customer_name')
admin.site.register(Invoice,InvoiceAdmin)

class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display=('invoice','description','quantity','unit_price','price')
admin.site.register(InvoiceDetail,InvoiceDetailAdmin)


