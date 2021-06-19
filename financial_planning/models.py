from django.db import models
from forex_python.converter import CurrencyRates

import requests

cc = CurrencyRates()

# url = 'https://v6.exchangerate-api.com/v6/47d50b6538abaa595f633cee/latest/BRL'

# response = requests.get(url)
# data = response.json()
# brl_to_uyu = data['conversion_rates']['UYU']

brl_to_cad = cc.convert('BRL', 'CAD', 1)
brl_to_nzd = cc.convert('BRL', 'NZD', 1)
brl_to_usd = cc.convert('BRL', 'USD', 1)
brl_to_uyu = 8.60

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