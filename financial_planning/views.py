from django.shortcuts import get_object_or_404, render
from django.views import View
from forex_python.converter import CurrencyRates
from pathlib import Path

import json
import pandas as pd
from pandas.io.parsers import read_csv

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
      'bills': self.bills(),
      'food': self.food(),
      'shopping': self.shopping(),
      'supermarket': self.supermarket(),
      'total_s_sp': self.total_s_sp(),
      'total_s_sp_cad': self.total_s_sp_cad(),
      'total_s_sp_nzd': self.total_s_sp_nzd(),
      'total_s_sp_usd': self.total_s_sp_usd(),
    }
    return render(request, template, context)
  
  def bills(self):
    cc = CurrencyRates()

    cad = cc.convert('BRL', 'CAD', 1)
    nzd = cc.convert('BRL', 'NZD', 1)
    usd = cc.convert('BRL', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/brazil/bills.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["USD"] = (c['Price (BRL)'] * usd).round().astype(int)
    c["CAD"] = (c['Price (BRL)'] * cad).round().astype(int)
    c["NZD"] = (c['Price (BRL)'] * nzd).round().astype(int)
    
    html_table = c.to_html(classes = 'bills', index = False)
    
    return html_table
  
  def food(self):
    cc = CurrencyRates()

    cad = cc.convert('BRL', 'CAD', 1)
    nzd = cc.convert('BRL', 'NZD', 1)
    usd = cc.convert('BRL', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/brazil/food.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["USD"] = (c['Price (BRL)'] * usd).round().astype(int)
    c["CAD"] = (c['Price (BRL)'] * cad).round().astype(int)
    c["NZD"] = (c['Price (BRL)'] * nzd).round().astype(int)
    
    html_table = c.to_html(classes = 'food', index = False)
    
    return html_table
  
  def shopping(self):
    cc = CurrencyRates()

    cad = cc.convert('BRL', 'CAD', 1)
    nzd = cc.convert('BRL', 'NZD', 1)
    usd = cc.convert('BRL', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/brazil/purchases.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["USD"] = (c['Price (BRL)'] * usd).round().astype(int)
    c["CAD"] = (c['Price (BRL)'] * cad).round().astype(int)
    c["NZD"] = (c['Price (BRL)'] * nzd).round().astype(int)
    
    html_table = c.to_html(classes = 'shopping', index = False)
    
    return html_table
  
  def supermarket(self):
    cc = CurrencyRates()

    cad = cc.convert('BRL', 'CAD', 1)
    nzd = cc.convert('BRL', 'NZD', 1)
    usd = cc.convert('BRL', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/brazil/supermarket.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["USD"] = (c['Price (BRL)'] * usd).round().astype(int)
    c["CAD"] = (c['Price (BRL)'] * cad).round().astype(int)
    c["NZD"] = (c['Price (BRL)'] * nzd).round().astype(int)
    
    html_table = c.to_html(classes = 'supermarket', index = False)
    
    return html_table
  
  def total_s_sp(self):
    base_path = Path(__file__).parent
    shopping = (base_path / "static/data/brazil/purchases.csv").resolve()
    supermarket = (base_path / "static/data/brazil/supermarket.csv").resolve()
    s = read_csv(shopping)
    sp = read_csv(supermarket)
    
    t = s["Price (BRL)"].sum() + sp["Price (BRL)"].sum()
    
    return t
  
  def total_s_sp_cad(self):
    t = self.total_s_sp()
    
    cc = CurrencyRates()
    cad = cc.convert('BRL', 'CAD', 1)
    
    tcad = (t * cad).round().astype(int)
    
    return tcad
  
  def total_s_sp_nzd(self):
    t = self.total_s_sp()
    
    cc = CurrencyRates()
    nzd = cc.convert('BRL', 'NZD', 1)
    
    tnzd = (t * nzd).round().astype(int)
    
    return tnzd
  
  def total_s_sp_usd(self):
    t = self.total_s_sp()
    
    cc = CurrencyRates()
    usd = cc.convert('BRL', 'USD', 1)
    
    tusd = (t * usd).round().astype(int)
    
    return tusd
