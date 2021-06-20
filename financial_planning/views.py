from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404, render
from django.views import View
from forex_python.converter import CurrencyRates
from .models import BrazilBill, BrazilFood, BrazilMedicaments, BrazilShopping, BrazilSupermarket
import requests

cc = CurrencyRates()

# brl = 'https://v6.exchangerate-api.com/v6/47d50b6538abaa595f633cee/latest/BRL'

# response = requests.get(brl)
# uy = response.json()
# uyu = uy['conversion_rates']['UYU']

brl_to_cad = cc.convert('BRL', 'CAD', 1)
brl_to_nzd = cc.convert('BRL', 'NZD', 1)
brl_to_usd = cc.convert('BRL', 'USD', 1)
brl_to_uyu = 8.60

class Mixin(object):
  def get_data(self):
    id = self.kwargs.get('id')
    obj = None
    if id is not None:
        obj = get_object_or_404(self.model, id = id)
    return obj
  
class financial_planning(Mixin, View):
  def get(self, request, id = None, *args, **kwargs):
    template = "pages/financial-planning.html"
    context = {
      'title': "Planejamentos financeiros",
      'brazil_bill': self.brazil_bill(),
      'brazil_bill_total_brl': self.brazil_bill_total_brl(),
      'brazil_bill_total_cad': self.brazil_bill_total_cad(),
      'brazil_bill_total_nzd': self.brazil_bill_total_nzd(),
      'brazil_bill_total_usd': self.brazil_bill_total_usd(),
      'brazil_bill_total_uyu': self.brazil_bill_total_uyu(),
      'brazil_shopping': self.brazil_shopping(),
      'brazil_shopping_total_brl': self.brazil_shopping_total_brl(),
      'brazil_shopping_total_cad': self.brazil_shopping_total_cad(),
      'brazil_shopping_total_nzd': self.brazil_shopping_total_nzd(),
      'brazil_shopping_total_usd': self.brazil_shopping_total_usd(),
      'brazil_shopping_total_uyu': self.brazil_shopping_total_uyu(),
      'brazil_food': self.brazil_food(),
      'brazil_food_total_brl': self.brazil_food_total_brl(),
      'brazil_food_total_cad': self.brazil_food_total_cad(),
      'brazil_food_total_nzd': self.brazil_food_total_nzd(),
      'brazil_food_total_usd': self.brazil_food_total_usd(),
      'brazil_food_total_uyu': self.brazil_food_total_uyu(),
      'brazil_medicaments': self.brazil_medicaments(),
      'brazil_medicaments_total_brl': self.brazil_medicaments_total_brl(),
      'brazil_medicaments_total_cad': self.brazil_medicaments_total_cad(),
      'brazil_medicaments_total_nzd': self.brazil_medicaments_total_nzd(),
      'brazil_medicaments_total_usd': self.brazil_medicaments_total_usd(),
      'brazil_medicaments_total_uyu': self.brazil_medicaments_total_uyu(),
      'brazil_supermarket': self.brazil_supermarket(),
      'brazil_supermarket_total_brl': self.brazil_supermarket_total_brl(),
      'brazil_supermarket_total_cad': self.brazil_supermarket_total_cad(),
      'brazil_supermarket_total_nzd': self.brazil_supermarket_total_nzd(),
      'brazil_supermarket_total_usd': self.brazil_supermarket_total_usd(),
      'brazil_supermarket_total_uyu': self.brazil_supermarket_total_uyu(),
      'brazil_total_brl': self.brazil_total_brl(),
      'brazil_total_cad': self.brazil_total_cad(),
      'brazil_total_nzd': self.brazil_total_nzd(),
      'brazil_total_usd': self.brazil_total_usd(),
      'brazil_total_uyu': self.brazil_total_uyu(),
    }
    return render(request, template, context)
  
  # Bills
  def brazil_bill(self):
    object_list = BrazilBill.objects.all().order_by('item')
    
    return object_list
  
  def brazil_bill_total_brl(self):
    return BrazilBill.objects.all().aggregate(Sum('price')).get('price__sum')
  
  def brazil_bill_total_cad(self):
    brl = self.brazil_bill_total_brl()
    total = float(brl) * brl_to_cad
    
    return round(total, 2)
  
  def brazil_bill_total_nzd(self):
    brl = self.brazil_bill_total_brl()
    total = float(brl) * brl_to_nzd
    
    return round(total, 2)
  
  def brazil_bill_total_usd(self):
    brl = self.brazil_bill_total_brl()
    total = float(brl) * brl_to_usd
    
    return round(total, 2)
  
  def brazil_bill_total_uyu(self):
    brl = self.brazil_bill_total_brl()
    total = float(brl) * brl_to_uyu
    
    return round(total, 2)

  # Food
  def brazil_food(self):
    object_list = BrazilFood.objects.all().order_by('item')
    
    return object_list
  
  def brazil_food_total_brl(self):
    return BrazilFood.objects.all().aggregate(Sum('price')).get('price__sum')
  
  def brazil_food_total_cad(self):
    brl = self.brazil_food_total_brl()
    total = float(brl) * brl_to_cad
    
    return round(total, 2)
  
  def brazil_food_total_nzd(self):
    brl = self.brazil_food_total_brl()
    total = float(brl) * brl_to_nzd
    
    return round(total, 2)
  
  def brazil_food_total_usd(self):
    brl = self.brazil_food_total_brl()
    total = float(brl) * brl_to_usd
    
    return round(total, 2)
  
  def brazil_food_total_uyu(self):
    brl = self.brazil_food_total_brl()
    total = float(brl) * brl_to_uyu
    
    return round(total, 2)
  
  # Medicaments
  def brazil_medicaments(self):
    object_list = BrazilMedicaments.objects.all().order_by('item')
    
    return object_list
  
  def brazil_medicaments_total_brl(self):
    return BrazilMedicaments.objects.all().aggregate(Sum('price')).get('price__sum')
  
  def brazil_medicaments_total_cad(self):
    brl = self.brazil_medicaments_total_brl()
    total = float(brl) * brl_to_cad
    
    return round(total, 2)
  
  def brazil_medicaments_total_nzd(self):
    brl = self.brazil_medicaments_total_brl()
    total = float(brl) * brl_to_nzd
    
    return round(total, 2)
  
  def brazil_medicaments_total_usd(self):
    brl = self.brazil_medicaments_total_brl()
    total = float(brl) * brl_to_usd
    
    return round(total, 2)
  
  def brazil_medicaments_total_uyu(self):
    brl = self.brazil_medicaments_total_brl()
    total = float(brl) * brl_to_uyu
    
    return round(total, 2)
  
  # Shopping
  def brazil_shopping(self):
    object_list = BrazilShopping.objects.all().order_by('item')
    
    return object_list
  
  def brazil_shopping_total_brl(self):
    return BrazilShopping.objects.all().aggregate(Sum('price')).get('price__sum')
  
  def brazil_shopping_total_cad(self):
    brl = self.brazil_shopping_total_brl()
    total = float(brl) * brl_to_cad
    
    return round(total, 2)
  
  def brazil_shopping_total_nzd(self):
    brl = self.brazil_shopping_total_brl()
    total = float(brl) * brl_to_nzd
    
    return round(total, 2)
  
  def brazil_shopping_total_usd(self):
    brl = self.brazil_shopping_total_brl()
    total = float(brl) * brl_to_usd
    
    return round(total, 2)
  
  def brazil_shopping_total_uyu(self):
    brl = self.brazil_shopping_total_brl()
    total = float(brl) * brl_to_uyu
    
    return round(total, 2)
  
  # Supermarkets
  def brazil_supermarket(self):
    object_list = BrazilSupermarket.objects.all().order_by('item')
    
    return object_list
  
  def brazil_supermarket_total_brl(self):
    return BrazilSupermarket.objects.all().aggregate(Sum('price')).get('price__sum')
  
  def brazil_supermarket_total_cad(self):
    brl = self.brazil_supermarket_total_brl()
    total = float(brl) * brl_to_cad
    
    return round(total, 2)
  
  def brazil_supermarket_total_nzd(self):
    brl = self.brazil_supermarket_total_brl()
    total = float(brl) * brl_to_nzd
    
    return round(total, 2)
  
  def brazil_supermarket_total_usd(self):
    brl = self.brazil_supermarket_total_brl()
    total = float(brl) * brl_to_usd
    
    return round(total, 2)
  
  def brazil_supermarket_total_uyu(self):
    brl = self.brazil_supermarket_total_brl()
    total = float(brl) * brl_to_uyu
    
    return round(total, 2)
  
  def brazil_total_brl(self):
    bills = self.brazil_bill_total_brl()
    food = self.brazil_food_total_brl()
    medicaments = self.brazil_medicaments_total_brl()
    shopping = self.brazil_shopping_total_brl()
    supermarket = self.brazil_supermarket_total_brl()
    
    total = bills + food + medicaments + shopping + supermarket
    
    return round(total, 2)
  
  def brazil_total_cad(self):
    brl = self.brazil_total_brl()
    total = float(brl) * brl_to_cad
    
    return round(total, 2)
  
  def brazil_total_nzd(self):
    brl = self.brazil_total_brl()
    total = float(brl) * brl_to_nzd
    
    return round(total, 2)
  
  def brazil_total_usd(self):
    brl = self.brazil_total_brl()
    total = float(brl) * brl_to_usd
    
    return round(total, 2)
  
  def brazil_total_uyu(self):
    brl = self.brazil_total_brl()
    total = float(brl) * brl_to_uyu
    
    return round(total, 2)