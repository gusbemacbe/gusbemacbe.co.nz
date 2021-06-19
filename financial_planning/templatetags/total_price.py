from django import template
from django.db.models import F, Sum
from financial_planning.models import BrazilBill
from forex_python.converter import CurrencyRates

import requests

register = template.Library()

cc = CurrencyRates()

cad = cc.convert('BRL', 'CAD', 1)
nzd = cc.convert('BRL', 'NZD', 1)
usd = cc.convert('BRL', 'USD', 1)

url = 'https://v6.exchangerate-api.com/v6/47d50b6538abaa595f633cee/latest/BRL'

response = requests.get(url)
data = response.json()
uyu = data['conversion_rates']['UYU']


@register.filter
def brazil_bill_total_brl(value):
    return BrazilBill.objects.aggregate(Sum('price')).get('price__sum')

@register.filter
def brazil_bill_total_cad(value):
    return round(float(brazil_bill_total_brl(value)) * cad, 2)

@register.filter
def brazil_bill_total_nzd(value):
    return round(float(brazil_bill_total_brl(value)) * nzd, 2)

@register.filter
def brazil_bill_total_usd(value):
    return round(float(brazil_bill_total_brl(value)) * usd, 2)

@register.filter
def brazil_bill_total_uyu(value):
    return round(float(brazil_bill_total_brl(value)) * uyu, 2)