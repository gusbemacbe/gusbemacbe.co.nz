from django.contrib import admin
from .models import BrazilBill

@admin.register(BrazilBill)
class BrazilBillAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'cad_price', 'nzd_price', 'usd_price', 'uyu_price')

