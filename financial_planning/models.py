from django.db import models
from forex_python.converter import CurrencyRates

import requests

class BrazilBill(models.Model):
  cc = CurrencyRates()
  
  cad = cc.convert('BRL', 'CAD', 1)
  nzd = cc.convert('BRL', 'NZD', 1)
  usd = cc.convert('BRL', 'USD', 1)
  
  url = 'https://v6.exchangerate-api.com/v6/47d50b6538abaa595f633cee/latest/BRL'
    
  response = requests.get(url)
  data = response.json()
  uyu = data['conversion_rates']['UYU']
    
  item = models.CharField('item', max_length = 50)
  price = models.DecimalField('price', max_digits = 10, decimal_places = 2)

  @property
  def cad_price(self):
      return round(float(self.price) * self.cad, 2)

  @property
  def nzd_price(self):
      return round(float(self.price) * self.nzd, 2)

  @property
  def usd_price(self):
      return round(float(self.price) * self.usd, 2)

  @property
  def uyu_price(self):
      return round(float(self.price) * self.uyu, 2)
    
  class Meta:
      verbose_name = 'Brazil\'s Bill'
      verbose_name_plural = 'Brazil\'s Bills'
  
  def __str__(self):
      return self.item