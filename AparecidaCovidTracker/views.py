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
    }
    return render(request, template, context)
  
  def today_cases(self):
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/prefeitura-de-aparecida/aparecida-small-without-duplicates.csv").resolve()
    s = pd.read_csv(file_path, parse_dates=['date'])
    pd.options.mode.chained_assignment = None
    city = s[s['city'] == 'Aparecida']
    today_city = city['totalCases'].values[-1]
    
    return today_city