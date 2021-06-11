from django.urls import path
from .views import financial_planning

urlpatterns = [ path('', financial_planning.as_view(), name='financial-planning')]