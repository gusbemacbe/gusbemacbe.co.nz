from django.shortcuts import get_object_or_404, render
from django.views import View

import json
from .models import Product

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
    }
    return render(request, template, context)