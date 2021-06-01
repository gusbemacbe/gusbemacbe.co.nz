from django.urls import path
from .views import AparecidaCovidTrackerView

urlpatterns = [ path('', AparecidaCovidTrackerView.as_view(), name='aparecida-covid-19-tracker')]