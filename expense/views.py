from django.shortcuts import render
from .models import Expense

# Create your views here.
def expense_list(request):
    template_name = 'pages/expense/expense_list.html'
    object_list = Expense.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def expense_detail(request, pk):
    template_name = 'pages/expense/expense_detail.html'
    return render(request, template_name)


def expense_create(request):
    template_name = 'pages/expense/expense_form.html'
    return render(request, template_name)
