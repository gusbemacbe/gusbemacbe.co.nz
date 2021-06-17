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
      'brazil_bills': self.brazil_bills(),
      'brazil_food': self.brazil_food(),
      'brazil_medicaments': self.brazil_medicaments(),
      'brazil_shopping': self.brazil_shopping(),
      'brazil_supermarket': self.brazil_supermarket(),
      'brazil_totalisation': self.brazil_totalisation(),
      'nz_bills': self.nz_bills(),
      'nz_food': self.nz_food(),
      'nz_office': self.nz_office(),
      'nz_pre_travel': self.nz_pre_travel(),
      'nz_shopping': self.nz_shopping(),
      'nz_supermarket': self.nz_supermarket(),
      'nz_totalisation': self.nz_totalisation(),
      'nz_comparison_minimum_wage': self.nz_comparison_minimum_wage(),
      'nz_comparison_minimum_wage_developer': self.nz_comparison_minimum_wage_developer(),
      'uy_pre_travel': self.uy_pre_travel(),
    }
    return render(request, template, context)
  
# region [ rgba(0, 39, 118, 0.1) ]
# Costs of living in Brazil

  def brazil_bills(self):
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
  
  def brazil_food(self):
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
  
  def brazil_medicaments(self):
    cc = CurrencyRates()

    cad = cc.convert('BRL', 'CAD', 1)
    nzd = cc.convert('BRL', 'NZD', 1)
    usd = cc.convert('BRL', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/brazil/medicaments.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["USD"] = (c['Price (BRL)'] * usd).round().astype(int)
    c["CAD"] = (c['Price (BRL)'] * cad).round().astype(int)
    c["NZD"] = (c['Price (BRL)'] * nzd).round().astype(int)
    
    html_table = c.to_html(classes = 'medicaments', index = False)
    
    return html_table
  
  def brazil_shopping(self):
    cc = CurrencyRates()

    cad = cc.convert('BRL', 'CAD', 1)
    nzd = cc.convert('BRL', 'NZD', 1)
    usd = cc.convert('BRL', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/brazil/shopping.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["USD"] = (c['Price (BRL)'] * usd).round().astype(int)
    c["CAD"] = (c['Price (BRL)'] * cad).round().astype(int)
    c["NZD"] = (c['Price (BRL)'] * nzd).round().astype(int)
    
    html_table = c.to_html(classes = 'shopping', index = False)
    
    return html_table
  
  def brazil_supermarket(self):
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
  
# endregion
  
# region [ rgba(204, 20, 43, 0.1) ]
# Costs of living in New Zealand

  def nz_pre_travel(self):
    
    cc = CurrencyRates()
    
    cad = cc.convert('BRL', 'CAD', 1)
    nzd = cc.convert('BRL', 'NZD', 1)
    usd = cc.convert('BRL', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/nz/pre-travel.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["CAD"] = (c['Price (BRL)'] * cad).round().astype(int)
    c["NZD"] = (c['Price (BRL)'] * nzd).round().astype(int)
    c["USD"] = (c['Price (BRL)'] * usd).round().astype(int)
    
    html_table = c.to_html(classes = 'pre-travel', index = False)
    
    return html_table

  def nz_bills(self):
    
    cc = CurrencyRates()
    
    brl = cc.convert('NZD', 'BRL', 1)
    cad = cc.convert('NZD', 'CAD', 1)
    usd = cc.convert('NZD', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/nz/bills.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["BRL"] = (c['Price (NZD)'] * brl).round().astype(int)
    c["CAD"] = (c['Price (NZD)'] * cad).round().astype(int)
    c["USD"] = (c['Price (NZD)'] * usd).round().astype(int)
    
    html_table = c.to_html(classes = 'bills', index = False)
    
    return html_table

  def nz_food(self):
    
    cc = CurrencyRates()
    
    brl = cc.convert('NZD', 'BRL', 1)
    cad = cc.convert('NZD', 'CAD', 1)
    usd = cc.convert('NZD', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/nz/food.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["BRL"] = (c['Price (NZD)'] * brl).round().astype(int)
    c["CAD"] = (c['Price (NZD)'] * cad).round().astype(int)
    c["USD"] = (c['Price (NZD)'] * usd).round().astype(int)
    
    html_table = c.to_html(classes = 'food', index = False)
    
    return html_table
  
  def nz_shopping(self):
    
    cc = CurrencyRates()
    
    brl = cc.convert('NZD', 'BRL', 1)
    cad = cc.convert('NZD', 'CAD', 1)
    usd = cc.convert('NZD', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/nz/shopping.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["BRL"] = (c['Price (NZD)'] * brl).round().astype(int)
    c["CAD"] = (c['Price (NZD)'] * cad).round().astype(int)
    c["USD"] = (c['Price (NZD)'] * usd).round().astype(int)
    
    html_table = c.to_html(classes = 'shopping', index = False)
    
    return html_table

  def nz_office(self):
    
    cc = CurrencyRates()
    
    brl = cc.convert('NZD', 'BRL', 1)
    cad = cc.convert('NZD', 'CAD', 1)
    usd = cc.convert('NZD', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/nz/office.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["BRL"] = (c['Price (NZD)'] * brl).round().astype(int)
    c["CAD"] = (c['Price (NZD)'] * cad).round().astype(int)
    c["USD"] = (c['Price (NZD)'] * usd).round().astype(int)
    
    html_table = c.to_html(classes = 'office', index = False)
    
    return html_table

  def nz_supermarket(self):
    
    cc = CurrencyRates()
    
    brl = cc.convert('NZD', 'BRL', 1)
    cad = cc.convert('NZD', 'CAD', 1)
    usd = cc.convert('NZD', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/nz/supermarket.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["BRL"] = (c['Price (NZD)'] * brl).round().astype(int)
    c["CAD"] = (c['Price (NZD)'] * cad).round().astype(int)
    c["USD"] = (c['Price (NZD)'] * usd).round().astype(int)
    
    html_table = c.to_html(classes = 'supermarket', index = False)
    
    return html_table
  
# endregion

# region [ rgba(123, 63, 0, 0.1) ]
# Costs of living in Uruguay

  def uy_pre_travel(self):
    
    cc = CurrencyRates()
    
    cad = cc.convert('BRL', 'CAD', 1)
    nzd = cc.convert('BRL', 'NZD', 1)
    usd = cc.convert('BRL', 'USD', 1)
    
    base_path = Path(__file__).parent
    file_path = (base_path / "static/data/nz/pre-travel.csv").resolve()
    c = pd.read_csv(file_path)
    c.loc["Total"] = c.sum()
    c["Item"].values[-1] = "Total"
    
    c["CAD"] = (c['Price (BRL)'] * cad).round().astype(int)
    c["NZD"] = (c['Price (BRL)'] * nzd).round().astype(int)
    c["USD"] = (c['Price (BRL)'] * usd).round().astype(int)
    
    html_table = c.to_html(classes = 'pre-travel', index = False)
    
    return html_table

# endregion

  def brazil_totalisation(self):
    cc = CurrencyRates()

    cad = cc.convert('BRL', 'CAD', 1)
    nzd = cc.convert('BRL', 'NZD', 1)
    usd = cc.convert('BRL', 'USD', 1)
    
    base_path = Path(__file__).parent
    bills = (base_path / "static/data/brazil/bills.csv").resolve()
    food = (base_path / "static/data/brazil/food.csv").resolve()
    medicaments = (base_path / "static/data/brazil/medicaments.csv").resolve()
    shopping = (base_path / "static/data/brazil/shopping.csv").resolve()
    supermarket = (base_path / "static/data/brazil/supermarket.csv").resolve()
    
    b = read_csv(bills)
    f = read_csv(food)
    m = read_csv(medicaments)
    s = read_csv(shopping)
    sp = read_csv(supermarket)
    
    b.loc["Total"] = b.sum()
    f.loc["Total"] = f.sum()
    m.loc["Total"] = m.sum()
    s.loc["Total"] = s.sum()
    sp.loc["Total"] = sp.sum()
    
    b_v = b.loc["Total"].values[1]
    f_v = f.loc["Total"].values[1]
    m_v = m.loc["Total"].values[1]
    s_v = s.loc["Total"].values[1]
    sp_v = sp.loc["Total"].values[1]
    
    t = b_v + f_v + m_v + s_v + sp_v
        
    usd_bills = (b_v * usd).round().astype(int)
    usd_food = (f_v * usd).round().astype(int)
    usd_medicaments = (m_v * usd).round().astype(int)
    usd_shopping = (s_v * usd).round().astype(int)
    usd_supermarket = (sp_v * usd).round().astype(int)
    usd_total = (t * usd).round().astype(int)

    cad_bills = (b_v * cad).round().astype(int)
    cad_food = (f_v * cad).round().astype(int)
    cad_medicaments = (m_v * cad).round().astype(int)
    cad_shopping = (s_v * cad).round().astype(int)
    cad_supermarket = (sp_v * cad).round().astype(int)
    cad_total = (t * cad).round().astype(int)

    nzd_bills = (b_v * nzd).round().astype(int)
    nzd_food = (f_v * nzd).round().astype(int)
    nzd_medicaments = (m_v * nzd).round().astype(int)
    nzd_shopping = (s_v * nzd).round().astype(int)
    nzd_supermarket = (sp_v * nzd).round().astype(int)
    nzd_total = (t * nzd).round().astype(int)
    
    data = {
        "List" : [ "Bills", "Food", "Medicaments", "Shopping", "Supermarket", "Total" ],
        "Total (BRL)": [ b_v, f_v, m_v, s_v, sp_v, t ],
        "USD": [  usd_bills, usd_food, usd_medicaments, usd_shopping, usd_supermarket, usd_total ],
        "CAD": [  cad_bills, cad_food, cad_medicaments, cad_shopping, cad_supermarket, cad_total ],
        "NZD": [  nzd_bills, nzd_food, nzd_medicaments, nzd_shopping, nzd_supermarket, nzd_total ]
    }
    
    df = pd.DataFrame(data)
    
    html_table = df.to_html(classes = 'totalisation', index = False)
    
    return html_table
  
  def nz_totalisation(self):
    cc = CurrencyRates()

    brl = cc.convert('NZD', 'BRL', 1)
    cad = cc.convert('NZD', 'CAD', 1)
    usd = cc.convert('NZD', 'USD', 1)
    
    base_path = Path(__file__).parent
    bills = (base_path / "static/data/nz/bills.csv").resolve()
    food = (base_path / "static/data/nz/food.csv").resolve()
    office = (base_path / "static/data/nz/office.csv").resolve()
    shopping = (base_path / "static/data/nz/shopping.csv").resolve()
    supermarket = (base_path / "static/data/nz/supermarket.csv").resolve()
    
    b = read_csv(bills)
    f = read_csv(food)
    o = read_csv(office)
    s = read_csv(shopping)
    sp = read_csv(supermarket)
    
    b.loc["Total"] = b.sum()
    f.loc["Total"] = f.sum()
    o.loc["Total"] = o.sum()
    s.loc["Total"] = s.sum()
    sp.loc["Total"] = sp.sum()
    
    b_v = b.loc["Total"].values[1]
    f_v = f.loc["Total"].values[1]
    o_v = o.loc["Total"].values[1]
    s_v = s.loc["Total"].values[1]
    sp_v = sp.loc["Total"].values[1]
    
    t = b_v + f_v + o_v + s_v + sp_v
    t_f = b_v + f_v + o_v + sp_v
        
    usd_bills = (b_v * usd).round().astype(int)
    usd_food = (f_v * usd).round().astype(int)
    usd_office = (o_v * usd).round().astype(int)
    usd_shopping = (s_v * usd).round().astype(int)
    usd_supermarket = (sp_v * usd).round().astype(int)
    usd_total_non_furnished = (t * usd).round().astype(int)
    usd_total_furnished = (t_f * usd).round().astype(int)

    cad_bills = (b_v * cad).round().astype(int)
    cad_food = (f_v * cad).round().astype(int)
    cad_office = (o_v * cad).round().astype(int)
    cad_shopping = (s_v * cad).round().astype(int)
    cad_supermarket = (sp_v * cad).round().astype(int)
    cad_total_non_furnished = (t * cad).round().astype(int)
    cad_total_furnished = (t_f * cad).round().astype(int)

    brl_bills = (b_v * brl).round().astype(int)
    brl_food = (f_v * brl).round().astype(int)
    brl_office = (o_v * brl).round().astype(int)
    brl_shopping = (s_v * brl).round().astype(int)
    brl_supermarket = (sp_v * brl).round().astype(int)
    brl_total_non_furnished = (t * brl).round().astype(int)
    brl_total_furnished = (t_f * brl).round().astype(int)
    
    data = {
        "List" : [ "Bills", "Food", "Medicaments", "Shopping", "Supermarket", "Total (non-furnished)", "Total (furnished)" ],
        "Total (NZD)": [ b_v, f_v, o_v, s_v, sp_v, t, t_f ],
        "USD": [  usd_bills, usd_food, usd_office, usd_shopping, usd_supermarket, usd_total_non_furnished, usd_total_furnished ],
        "CAD": [  cad_bills, cad_food, cad_office, cad_shopping, cad_supermarket, cad_total_non_furnished, cad_total_furnished ],
        "BRL": [  brl_bills, brl_food, brl_office, brl_shopping, brl_supermarket, brl_total_non_furnished, brl_total_furnished ]
    }
    
    df = pd.DataFrame(data)
    
    html_table = df.to_html(classes = 'totalisation', index = False)
    
    return html_table
  
  def nz_comparison_minimum_wage(self):
    base_path = Path(__file__).parent
    bills = (base_path / "static/data/nz/bills.csv").resolve()
    food = (base_path / "static/data/nz/food.csv").resolve()
    
    b = read_csv(bills)
    f = read_csv(food)
    
    b.loc["Total"] = b.sum()
    f.loc["Total"] = f.sum()
    
    b_v = b.loc["Total"].values[1]
    f_v = f.loc["Total"].values[1]
    
    t = b_v + f_v
    
    # Furnished flat rent cost
    r = 350 * 4
    
    # Minimum wage per hout
    adult_hour = 20
    trainee_hour = 16
    
    # Per month
    amw = (adult_hour * 40) * 4
    tmw = (trainee_hour * 40) * 4
    
    rn1 = amw - t - r
    rn2 = tmw - t - r
    
    data = {
        "List" : [ "Monthly Bills", "Rent", "General adult wage", "Remnant", "General trainee wage", "Remnant" ],
        "NZD": [ t, r, amw, rn1, tmw, rn2 ],
    }
    
    df = pd.DataFrame(data)
    
    html_table = df.to_html(classes = 'comparison-1', index = False)
    
    return html_table
  
  def nz_comparison_minimum_wage_developer(self):
    base_path = Path(__file__).parent
    bills = (base_path / "static/data/nz/bills.csv").resolve()
    food = (base_path / "static/data/nz/food.csv").resolve()
    
    b = read_csv(bills)
    f = read_csv(food)
    
    b.loc["Total"] = b.sum()
    f.loc["Total"] = f.sum()
    
    b_v = b.loc["Total"].values[1]
    f_v = f.loc["Total"].values[1]
    
    t = b_v + f_v
    
    # Furnished flat rent cost
    r = 350 * 4
    
    # Average salary of a developer in New Zealand
    minimum = 50000
    average = 65000
    maximium = 95000
    
    # Per month
    average_monthly_salary = int((average / 12))
    maximium_monthly_salary = int((maximium / 12))
    minimum_monthly_salary = int((minimum / 12))
    
    rn = average_monthly_salary - t - r
    
    data = {
        "List" : [ "Monthly Bills", "Rent", "Wage", "Remnant" ],
        "NZD": [ t, r, average_monthly_salary, rn ],
    }
    
    df = pd.DataFrame(data)
    
    html_table = df.to_html(classes = 'comparison-2', index = False)
    
    return html_table