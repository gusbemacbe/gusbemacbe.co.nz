from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Product
from pathlib import Path

import json
import pandas as pd

class Mixin(object):
  def get_data(self):
    id = self.kwargs.get('id')
    obj = None
    if id is not None:
        obj = get_object_or_404(self.model, id = id)
    return obj
      
class AparecidaCovidTrackerView(Mixin, View):
  def get(self, request, id = None, *args, **kwargs):
    template = "pages/aparecida-covid-19-tracker.html"
    queryset = Product.objects.all()
    names = [obj.name for obj in queryset]
    prices = [int(obj.price) for obj in queryset]
    context = {
      'title': "Painel Covidólogico de Aparecida",
      'names': json.dumps(names),
      'prices': json.dumps(prices),
      'today_cases': self.today_cases(),
      'today_new_cases': self.today_new_cases(),
      'today_active_cases': self.today_active_cases(),
      'today_deaths': self.today_deaths(),
      'today_new_deaths': self.today_new_deaths(),
      'today_recovered': self.today_recovered(),
      'today_new_recovered': self.today_new_recovered(),
      'today_busy_beds': self.today_busy_beds(),
      'today_new_busy_beds': self.today_new_busy_beds(),
      'today_ICUs': self.today_ICUs(),
      'today_new_ICUs': self.today_new_ICUs(),
      'condition_cases': self.condition_new_cases(),
      'condition_deaths': self.condition_new_deaths(),
      'condition_beds': self.condition_busy_beds(),
      'condition_ICUs': self.condition_ICUs(),
    }
    return render(request, template, context)
  
  def get_csv_file(self):
      base_path = Path(__file__).parent
      file_path = (base_path / "static/data/prefeitura-de-aparecida/aparecida-small-without-duplicates.csv").resolve()
      s = pd.read_csv(file_path, parse_dates=['date'])
      pd.options.mode.chained_assignment = None
      return s

# Total and daily numbers

  def today_cases(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['totalCases'].values[-1]
    
    return today

  def today_new_cases(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['totalCases'].values[-1] - city['totalCases'].values[-2]
    
    return today
  
  def today_active_cases(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['totalCases'].values[-1] - city['totalRecovered'].values[-1]
    
    return today
  
  def today_deaths(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['totalDeaths'].values[-1]
    
    return today

  def today_new_deaths(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['totalDeaths'].values[-1] - city['totalDeaths'].values[-2]
    
    return today
  
  def today_recovered(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['totalRecovered'].values[-1]
    
    return today
  
  def today_new_recovered(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['totalRecovered'].values[-1] - city['totalRecovered'].values[-2]
    
    return today
  
  def today_busy_beds(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['totalBeds'].values[-1]
    
    return today
  
  def today_new_busy_beds(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['totalBeds'].values[-1] - city['totalBeds'].values[-2]
    
    return today
  
  def today_ICUs(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['intubated'].values[-1]
    
    return today
  
  def today_new_ICUs(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    today = city['intubated'].values[-1] - city['intubated'].values[-2]
    
    return today
  
# Check the condition if it is high, stable and falling

  def condition_new_cases(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    val1 = city['totalCases'].values[-1]
    val2 = city['totalCases'].values[-2]
    
    if (val2 > val1):
      colour = "fall"
    elif (val2 == val1):
      colour = "stability"
    else:
      colour = "high"
    
    return colour

  def condition_new_deaths(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    val1 = city['totalDeaths'].values[-1]
    val2 = city['totalDeaths'].values[-2]
    
    if (val2 > val1):
      colour = "fall"
    elif (val2 == val1):
      colour = "stability"
    else:
      colour = "high"
    
    return colour
  
  def condition_busy_beds(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    val1 = city['totalBeds'].values[-1]
    val2 = city['totalBeds'].values[-2]
    
    if (val2 > val1):
      colour = "fall"
    elif (val2 == val1):
      colour = "stability"
    else:
      colour = "high"
    
    return colour
  
  def condition_ICUs(self):
    s = self.get_csv_file()
    city = s[s['city'] == 'Aparecida']
    val1 = city['intubated'].values[-1]
    val2 = city['intubated'].values[-2]
    
    if (val2 > val1):
      colour = "fall"
    elif (val2 == val1):
      colour = "stability"
    else:
      colour = "high"
    
    return colour