from django.shortcuts import get_object_or_404, render
from django.views import View

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
    context = {
      'title': "Painel Covidólogico de Aparecida",
    }
    return render(request, template, context)