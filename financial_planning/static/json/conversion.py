import json

currencies = ["BRL", "NZD", "UYU"]

# file = 'BRL.json'

# response = open(file)
# data = json.load(response)
# brl_to_uyu = data['conversion_rates']['UYU']

# print(5 * brl_to_uyu)

for currency in currencies:
  file = f'{currency}.json'
  
  response = open(file)
  data = json.load(response)
  to = data['conversion_rates']['UYU']
  print(f"{currency} to UYU: {1 * to}")