from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404, render
from django.views import View
from forex_python.converter import CurrencyRates
from pathlib import Path
from .models import BrazilBill, BrazilFood, BrazilMedicaments, BrazilShopping, BrazilSupermarket, NZBill, NZFood, NZOffice, NZPreTravel, NZShopping, NZSupermarket
import json

cc = CurrencyRates()

base_path = Path(__file__).parent

brlf = (base_path / "static/json/BRL.json").resolve()
nzdf = (base_path / "static/json/NZD.json").resolve()
uyuf = (base_path / "static/json/UYU.json").resolve()

brl_data = json.load(open(brlf))
nzd_data = json.load(open(nzdf))
uyu_data = json.load(open(uyuf))

# Convert the Brazil currency to CAD, NZD, USD and UYU
brl_to_cad = cc.convert('BRL', 'CAD', 1)
brl_to_nzd = cc.convert('BRL', 'NZD', 1)
brl_to_usd = cc.convert('BRL', 'USD', 1)
brl_to_uyu = brl_data['conversion_rates']['UYU']

# Convert New Zealander dollar to BRL, CAD, U and UYU
nzd_to_brl = cc.convert('NZD', 'BRL', 1)
nzd_to_cad = cc.convert('NZD', 'CAD', 1)
nzd_to_usd = cc.convert('NZD', 'USD', 1)
nzd_to_uyu = nzd_data['conversion_rates']['UYU']

# Average and trainee salary in New Zealand
nz_adult_hour = 20
nz_trainee_hour = 16

def week(hour):
  week = hour * 40
  return week

def month(hour):
  month = week(hour) * 4
  return month

def year(hour):
  year = month(hour) * 12
  return year

def formatter(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', ' mil', ' milhões', ' bilhões', ' trilhões', 'quatrilhões', 'quintilhões', 'sextilhões', 'septilhões', 'octilhões', 'nonilhões', 'decilhões', ][magnitude])

# Mininum, average and maximum salary of a developer in New Zealand
nz_minimum_developer_hour = 19.89
nz_average_developer_hour = 21.50
nz_maximum_developer_hour = 23.46

# Rent
nz_minimum_week_rent = 300
nz_maximum_week_rent = 400

nz_minimum_month_rent = nz_minimum_week_rent * 5
nz_maximum_month_rent = nz_maximum_week_rent * 5

# Rent in Ponsorby, Auckland
nz_minimum_week_rent_ponsorby = 440
nz_maximum_week_rent_ponsorby = 550

nz_minimum_month_rent_ponsorby = nz_minimum_week_rent_ponsorby * 5
nz_maximum_month_rent_ponsorby = nz_maximum_week_rent_ponsorby * 5

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
      'nz_bill': self.nz_bill(),
      'nz_bill_total_nzd': self.nz_bill_total_nzd(),
      'nz_bill_total_brl': self.nz_bill_total_brl(),
      'nz_bill_total_cad': self.nz_bill_total_cad(),
      'nz_bill_total_usd': self.nz_bill_total_usd(),
      'nz_bill_total_uyu': self.nz_bill_total_uyu(),
      'nz_food': self.nz_food(),
      'nz_food_total_nzd': self.nz_food_total_nzd(),
      'nz_food_total_brl': self.nz_food_total_brl(),
      'nz_food_total_cad': self.nz_food_total_cad(),
      'nz_food_total_usd': self.nz_food_total_usd(),
      'nz_food_total_uyu': self.nz_food_total_uyu(),
      'nz_food': self.nz_food(),
      'nz_food_total_nzd': self.nz_food_total_nzd(),
      'nz_food_total_brl': self.nz_food_total_brl(),
      'nz_food_total_cad': self.nz_food_total_cad(),
      'nz_food_total_usd': self.nz_food_total_usd(),
      'nz_food_total_uyu': self.nz_food_total_uyu(),
      'nz_office': self.nz_office(),
      'nz_office_total_nzd': self.nz_office_total_nzd(),
      'nz_office_total_brl': self.nz_office_total_brl(),
      'nz_office_total_cad': self.nz_office_total_cad(),
      'nz_office_total_usd': self.nz_office_total_usd(),
      'nz_office_total_uyu': self.nz_office_total_uyu(),
      'nz_pre_travel': self.nz_pre_travel(),
      'nz_pre_travel_total_brl': self.nz_pre_travel_total_brl(),
      'nz_pre_travel_total_cad': self.nz_pre_travel_total_cad(),
      'nz_pre_travel_total_nzd': self.nz_pre_travel_total_nzd(),
      'nz_pre_travel_total_usd': self.nz_pre_travel_total_usd(),
      'nz_pre_travel_total_uyu': self.nz_pre_travel_total_uyu(),
      'nz_shopping': self.nz_shopping(),
      'nz_shopping_total_nzd': self.nz_shopping_total_nzd(),
      'nz_shopping_total_brl': self.nz_shopping_total_brl(),
      'nz_shopping_total_cad': self.nz_shopping_total_cad(),
      'nz_shopping_total_usd': self.nz_shopping_total_usd(),
      'nz_shopping_total_uyu': self.nz_shopping_total_uyu(),
      'nz_supermarket': self.nz_supermarket(),
      'nz_supermarket_total_nzd': self.nz_supermarket_total_nzd(),
      'nz_supermarket_total_brl': self.nz_supermarket_total_brl(),
      'nz_supermarket_total_cad': self.nz_supermarket_total_cad(),
      'nz_supermarket_total_usd': self.nz_supermarket_total_usd(),
      'nz_supermarket_total_uyu': self.nz_supermarket_total_uyu(),
      'nz_total_nzd': self.nz_total_nzd(),
      'nz_total_brl': self.nz_total_brl(),
      'nz_total_cad': self.nz_total_cad(),
      'nz_total_usd': self.nz_total_usd(),
      'nz_total_uyu': self.nz_total_uyu(),
      'nz_total_furnished_nzd': self.nz_total_furnished_nzd(),
      'nz_total_furnished_brl': self.nz_total_furnished_brl(),
      'nz_total_furnished_cad': self.nz_total_furnished_cad(),
      'nz_total_furnished_usd': self.nz_total_furnished_usd(),
      'nz_total_furnished_uyu': self.nz_total_furnished_uyu(),
      'nzd_to_brl': nzd_to_brl,
      'nzd_to_cad': nzd_to_cad,
      'nzd_to_usd': nzd_to_usd,
      'nzd_to_uyu': nzd_to_uyu,
      'nz_adult_hour': nz_adult_hour,
      'nz_trainee_hour': nz_trainee_hour,
      'nz_minimum_developer_hour': nz_minimum_developer_hour,
      'nz_average_developer_hour': nz_average_developer_hour,
      'nz_maximum_developer_hour': nz_maximum_developer_hour,
      'nz_monthly_totalisation_nzd': self.nz_monthly_totalisation_nzd(),
      'nz_monthly_totalisation_brl': self.nz_monthly_totalisation_brl(),
      'nz_monthly_totalisation_cad': self.nz_monthly_totalisation_cad(),
      'nz_monthly_totalisation_usd': self.nz_monthly_totalisation_usd(),
      'nz_monthly_totalisation_uyu': self.nz_monthly_totalisation_uyu(),
      'nz_minimum_week_rent': nz_minimum_week_rent,
      'nz_maximum_week_rent': nz_maximum_week_rent,
      'nz_minimum_month_rent': nz_minimum_month_rent,
      'nz_maximum_month_rent': nz_maximum_month_rent,
      'nz_minimum_week_rent_ponsorby': nz_minimum_week_rent_ponsorby,
      'nz_maximum_week_rent_ponsorby': nz_maximum_week_rent_ponsorby,
      'nz_minimum_month_rent_ponsorby': nz_minimum_month_rent_ponsorby,
      'nz_maximum_month_rent_ponsorby': nz_minimum_month_rent_ponsorby,
    }
    return render(request, template, context)

# region [ rgba(0, 39, 118, 0.1) ]
## Brazil
  
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
  # endregion
  
# region [ rgba(204, 119, 34, 0.1) ]
## New Zealand

  # Pre-Travel
  def nz_pre_travel(self):
    object_list = NZPreTravel.objects.all().order_by('item')
    
    return object_list
  
  def nz_pre_travel_total_brl(self):
    return NZPreTravel.objects.all().aggregate(Sum('price')).get('price__sum')
  
  def nz_pre_travel_total_cad(self):
    brl = self.nz_pre_travel_total_brl()
    total = float(brl) * brl_to_cad
    
    return round(total, 2)
  
  def nz_pre_travel_total_nzd(self):
    brl = self.nz_pre_travel_total_brl()
    total = float(brl) * brl_to_nzd
    
    return round(total, 2)
  
  def nz_pre_travel_total_usd(self):
    brl = self.nz_pre_travel_total_brl()
    total = float(brl) * brl_to_usd
    
    return round(total, 2)
  
  def nz_pre_travel_total_uyu(self):
    brl = self.nz_pre_travel_total_brl()
    total = float(brl) * brl_to_uyu
    
    return round(total, 2)
  
  # Bills
  def nz_bill(self):
    object_list = NZBill.objects.all().order_by('item')
    
    return object_list
  
  def nz_bill_total_nzd(self):
    return round(NZBill.objects.all().aggregate(Sum('price')).get('price__sum'), 2)
  
  def nz_bill_total_brl(self):
    nzd = self.nz_bill_total_nzd()
    total = float(nzd) * nzd_to_brl
    
    return round(total, 2)
  
  def nz_bill_total_cad(self):
    nzd = self.nz_bill_total_nzd()
    total = float(nzd) * nzd_to_cad
    
    return round(total, 2)
  
  def nz_bill_total_usd(self):
    nzd = self.nz_bill_total_nzd()
    total = float(nzd) * nzd_to_usd
    
    return round(total, 2)
  
  def nz_bill_total_uyu(self):
    nzd = self.nz_bill_total_nzd()
    total = float(nzd) * nzd_to_uyu
    
    return round(total, 2)
  
  # Food
  def nz_food(self):
    object_list = NZFood.objects.all().order_by('item')
    
    return object_list
  
  def nz_food_total_nzd(self):
    total = NZFood.objects.all().aggregate(Sum('price')).get('price__sum')
    
    return round(total, 2)
  
  def nz_food_total_brl(self):
    nzd = self.nz_food_total_nzd()
    total = float(nzd) * nzd_to_brl
    
    return round(total, 2)
  
  def nz_food_total_cad(self):
    nzd = self.nz_food_total_nzd()
    total = float(nzd) * nzd_to_cad
    
    return round(total, 2)
  
  def nz_food_total_usd(self):
    nzd = self.nz_food_total_nzd()
    total = float(nzd) * nzd_to_usd
    
    return round(total, 2)
  
  def nz_food_total_uyu(self):
    nzd = self.nz_food_total_nzd()
    total = float(nzd) * nzd_to_uyu
    
    return round(total, 2)

  # Office
  def nz_office(self):
    object_list = NZOffice.objects.all().order_by('item')
    
    return object_list
  
  def nz_office_total_nzd(self):
    return round(NZOffice.objects.all().aggregate(Sum('price')).get('price__sum'), 2)
  
  def nz_office_total_brl(self):
    nzd = self.nz_office_total_nzd()
    total = float(nzd) * nzd_to_brl
    
    return round(total, 2)
  
  def nz_office_total_cad(self):
    nzd = self.nz_office_total_nzd()
    total = float(nzd) * nzd_to_cad
    
    return round(total, 2)
  
  def nz_office_total_usd(self):
    nzd = self.nz_office_total_nzd()
    total = float(nzd) * nzd_to_usd
    
    return round(total, 2)
  
  def nz_office_total_uyu(self):
    nzd = self.nz_office_total_nzd()
    total = float(nzd) * nzd_to_uyu
    
    return round(total, 2)
   
  # Shopping
  def nz_shopping(self):
    object_list = NZShopping.objects.all().order_by('item')
    
    return object_list
  
  def nz_shopping_total_nzd(self):
    return round(NZShopping.objects.all().aggregate(Sum('price')).get('price__sum'), 2)
  
  def nz_shopping_total_brl(self):
    nzd = self.nz_shopping_total_nzd()
    total = float(nzd) * nzd_to_brl
    
    return round(total, 2)
  
  def nz_shopping_total_cad(self):
    nzd = self.nz_shopping_total_nzd()
    total = float(nzd) * nzd_to_cad
    
    return round(total, 2)
  
  def nz_shopping_total_usd(self):
    nzd = self.nz_shopping_total_nzd()
    total = float(nzd) * nzd_to_usd
    
    return round(total, 2)
  
  def nz_shopping_total_uyu(self):
    nzd = self.nz_shopping_total_nzd()
    total = float(nzd) * nzd_to_uyu
    
    return round(total, 2)
   
  # Supermarket
  def nz_supermarket(self):
    object_list = NZSupermarket.objects.all().order_by('item')
    
    return object_list
  
  def nz_supermarket_total_nzd(self):
    return round(NZSupermarket.objects.all().aggregate(Sum('price')).get('price__sum'), 2)
  
  def nz_supermarket_total_brl(self):
    nzd = self.nz_supermarket_total_nzd()
    total = float(nzd) * nzd_to_brl
    
    return round(total, 2)
  
  def nz_supermarket_total_cad(self):
    nzd = self.nz_supermarket_total_nzd()
    total = float(nzd) * nzd_to_cad
    
    return round(total, 2)
  
  def nz_supermarket_total_usd(self):
    nzd = self.nz_supermarket_total_nzd()
    total = float(nzd) * nzd_to_usd
    
    return round(total, 2)
  
  def nz_supermarket_total_uyu(self):
    nzd = self.nz_supermarket_total_nzd()
    total = float(nzd) * nzd_to_uyu
    
    return round(total, 2)
  
  # Totalisation – Non-furnished
  def nz_total_nzd(self):
    bills = self.nz_bill_total_nzd()
    food = self.nz_food_total_nzd()
    office = self.nz_office_total_nzd()
    shopping = self.nz_shopping_total_nzd()
    supermarket = self.nz_supermarket_total_nzd()
    
    total = bills + food + office + shopping + supermarket
    
    return round(total, 2)
  
  def nz_total_brl(self):
    nzd = self.nz_total_nzd()
    total = float(nzd) * nzd_to_brl
    
    return round(total, 2)
  
  def nz_total_cad(self):
    nzd = self.nz_total_nzd()
    total = float(nzd) * nzd_to_cad
    
    return round(total, 2)
  
  def nz_total_usd(self):
    nzd = self.nz_total_nzd()
    total = float(nzd) * nzd_to_usd
    
    return round(total, 2)
  
  def nz_total_uyu(self):
    nzd = self.nz_total_nzd()
    total = float(nzd) * nzd_to_uyu
    
    return round(total, 2)
  
  # Totalisation – Furnished
  def nz_total_furnished_nzd(self):
    bills = self.nz_bill_total_nzd()
    food = self.nz_food_total_nzd()
    supermarket = self.nz_supermarket_total_nzd()
    
    total = bills + food + supermarket
    
    return round(total, 2)
  
  def nz_total_furnished_brl(self):
    nzd = self.nz_total_furnished_nzd()
    total = float(nzd) * nzd_to_brl
    
    return round(total, 2)
  
  def nz_total_furnished_cad(self):
    nzd = self.nz_total_furnished_nzd()
    total = float(nzd) * nzd_to_cad
    
    return round(total, 2)
  
  def nz_total_furnished_usd(self):
    nzd = self.nz_total_furnished_nzd()
    total = float(nzd) * nzd_to_usd
    
    return round(total, 2)
  
  def nz_total_furnished_uyu(self):
    nzd = self.nz_total_furnished_nzd()
    total = float(nzd) * nzd_to_uyu
    
    return round(total, 2)
  
  # Monhtly Totalisation
  def nz_monthly_totalisation_nzd(self):
    bills = self.nz_bill_total_nzd()
    food = self.nz_food_total_nzd()
    
    total = bills + food
     
    return round(total, 2)
  
  def nz_monthly_totalisation_brl(self):
    nzd = self.nz_monthly_totalisation_nzd()
    total = float(nzd) * nzd_to_brl
    
    return round(total, 2)
  
  def nz_monthly_totalisation_cad(self):
    nzd = self.nz_monthly_totalisation_nzd()
    total = float(nzd) * nzd_to_cad
    
    return round(total, 2)
  
  def nz_monthly_totalisation_usd(self):
    nzd = self.nz_monthly_totalisation_nzd()
    total = float(nzd) * nzd_to_usd
    
    return round(total, 2)
  
  def nz_monthly_totalisation_uyu(self):
    nzd = self.nz_monthly_totalisation_nzd()
    total = float(nzd) * nzd_to_uyu
    
    return round(total, 2)
  
  # endregion