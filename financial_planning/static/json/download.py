import json, requests

currencies = ["BRL", "NZD", "UYU"]

for currency in currencies:
  r = requests.get(f"https://v6.exchangerate-api.com/v6/47d50b6538abaa595f633cee/latest/{currency}")
  json_str = json.dumps(r.json())
  
  with open(f"{currency}.json", 'w') as f:
    f.write(json_str)