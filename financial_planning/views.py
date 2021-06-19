from django.db.models import Sum
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import BrazilBill

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
      'brazil_bills': self.brazil_bills(),
    }
    return render(request, template, context)
  
  def brazil_bills(self):
    object_list = BrazilBill.objects.all()
    
    return object_list
