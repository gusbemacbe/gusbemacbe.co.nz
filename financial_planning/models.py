from django.db import models
from forex_python.converter import CurrencyRates
from pathlib import Path

import json, requests

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

# Convert New Zealander dollar to BRL, CAD and UYU
nzd_to_brl = cc.convert('NZD', 'BRL', 1)
nzd_to_cad = cc.convert('NZD', 'CAD', 1)
nzd_to_usd = cc.convert('NZD', 'USD', 1)
nzd_to_uyu = nzd_data['conversion_rates']['UYU']


# region [ rgba(0, 39, 118, 0.1) ]
## Brazil
class BrazilBill(models.Model):
    
  item = models.CharField('item', max_length = 50)
  price = models.DecimalField('price', max_digits = 10, decimal_places = 2)

  @property
  def cad_price(self):
      return round(float(self.price) * brl_to_cad, 2)

  @property
  def nzd_price(self):
      return round(float(self.price) * brl_to_nzd, 2)

  @property
  def usd_price(self):
      return round(float(self.price) * brl_to_usd, 2)

  @property
  def uyu_price(self):
      return round(float(self.price) * brl_to_uyu, 2)
    
  class Meta:
      verbose_name = 'Brazil\'s Bill'
      verbose_name_plural = 'Brazil\'s Bills'
  
  def __str__(self):
      return self.item
  
class BrazilFood(models.Model):
    
  item = models.CharField('item', max_length = 50)
  price = models.DecimalField('price', max_digits = 10, decimal_places = 2)

  @property
  def cad_price(self):
      return round(float(self.price) * brl_to_cad, 2)

  @property
  def nzd_price(self):
      return round(float(self.price) * brl_to_nzd, 2)

  @property
  def usd_price(self):
      return round(float(self.price) * brl_to_usd, 2)

  @property
  def uyu_price(self):
      return round(float(self.price) * brl_to_uyu, 2)
    
  class Meta:
      verbose_name = 'Brazil\'s Food'
      verbose_name_plural = 'Brazil\'s Foods'
  
  def __str__(self):
      return self.item
  
class BrazilMedicaments(models.Model):
    
  item = models.CharField('item', max_length = 50)
  price = models.DecimalField('price', max_digits = 10, decimal_places = 2)

  @property
  def cad_price(self):
      return round(float(self.price) * brl_to_cad, 2)

  @property
  def nzd_price(self):
      return round(float(self.price) * brl_to_nzd, 2)

  @property
  def usd_price(self):
      return round(float(self.price) * brl_to_usd, 2)

  @property
  def uyu_price(self):
      return round(float(self.price) * brl_to_uyu, 2)
    
  class Meta:
      verbose_name = 'Brazil\'s Medicament'
      verbose_name_plural = 'Brazil\'s Medicaments'
  
  def __str__(self):
      return self.item

class BrazilShopping(models.Model):
    
  item = models.CharField('item', max_length = 50)
  price = models.DecimalField('price', max_digits = 10, decimal_places = 2)

  @property
  def cad_price(self):
      return round(float(self.price) * brl_to_cad, 2)

  @property
  def nzd_price(self):
      return round(float(self.price) * brl_to_nzd, 2)

  @property
  def usd_price(self):
      return round(float(self.price) * brl_to_usd, 2)

  @property
  def uyu_price(self):
      return round(float(self.price) * brl_to_uyu, 2)
    
  class Meta:
      verbose_name = 'Brazil\'s Shopping'
      verbose_name_plural = 'Brazil\'s Shoppings'
  
  def __str__(self):
      return self.item

class BrazilSupermarket(models.Model):
    
  item = models.CharField('item', max_length = 50)
  price = models.DecimalField('price', max_digits = 10, decimal_places = 2)

  @property
  def cad_price(self):
      return round(float(self.price) * brl_to_cad, 2)

  @property
  def nzd_price(self):
      return round(float(self.price) * brl_to_nzd, 2)

  @property
  def usd_price(self):
      return round(float(self.price) * brl_to_usd, 2)

  @property
  def uyu_price(self):
      return round(float(self.price) * brl_to_uyu, 2)
    
  class Meta:
      verbose_name = 'Brazil\'s Supermarket'
      verbose_name_plural = 'Brazil\'s Supermarket'
  
  def __str__(self):
      return self.item
  
# endregion

# region [ rgba() ]
## New Zealand
class NZPreTravel(models.Model):
    
  item = models.CharField('item', max_length = 50)
  price = models.DecimalField('price', max_digits = 10, decimal_places = 2)

  @property
  def cad_price(self):
      return round(float(self.price) * brl_to_cad, 2)

  @property
  def nzd_price(self):
      return round(float(self.price) * brl_to_nzd, 2)

  @property
  def usd_price(self):
      return round(float(self.price) * brl_to_usd, 2)

  @property
  def uyu_price(self):
      return round(float(self.price) * brl_to_uyu, 2)
    
  class Meta:
      verbose_name = 'New Zealand\'s Pre-Travel'
      verbose_name_plural = 'New Zealand\'s Pre-Travel'
  
  def __str__(self):
      return self.item
  
class NZBill(models.Model):
    
  item = models.CharField('item', max_length = 50)
  price = models.DecimalField('price', max_digits = 10, decimal_places = 2)

  @property
  def brl_price(self):
      return round(float(self.price) * nzd_to_brl, 2)

  @property
  def cad_price(self):
      return round(float(self.price) * nzd_to_cad, 2)

  @property
  def usd_price(self):
      return round(float(self.price) * nzd_to_usd, 2)

  @property
  def uyu_price(self):
      return round(float(self.price) * nzd_to_uyu, 2)
    
  class Meta:
      verbose_name = 'New Zealand\'s Bill'
      verbose_name_plural = 'New Zealand\'s Bills'
  
  def __str__(self):
      return self.item
  
class NZFood(models.Model):
    
  item = models.CharField('item', max_length = 50)
  price = models.DecimalField('price', max_digits = 10, decimal_places = 2)

  @property
  def brl_price(self):
      return round(float(self.price) * nzd_to_brl, 2)

  @property
  def cad_price(self):
      return round(float(self.price) * nzd_to_cad, 2)

  @property
  def usd_price(self):
      return round(float(self.price) * nzd_to_usd, 2)

  @property
  def uyu_price(self):
      return round(float(self.price) * nzd_to_uyu, 2)
    
  class Meta:
      verbose_name = 'New Zealand\'s Food'
      verbose_name_plural = 'New Zealand\'s Foods'
  
  def __str__(self):
      return self.item
  
class NZShopping(models.Model):
    
  item = models.CharField('item', max_length = 50)
  price = models.DecimalField('price', max_digits = 10, decimal_places = 2)

  @property
  def brl_price(self):
      return round(float(self.price) * nzd_to_brl, 2)

  @property
  def cad_price(self):
      return round(float(self.price) * nzd_to_cad, 2)

  @property
  def usd_price(self):
      return round(float(self.price) * nzd_to_usd, 2)

  @property
  def uyu_price(self):
      return round(float(self.price) * nzd_to_uyu, 2)
    
  class Meta:
      verbose_name = 'New Zealand\'s Shopping'
      verbose_name_plural = 'New Zealand\'s Shopping'
  
  def __str__(self):
      return self.item