import os

currencies = ["BRL", "NZD", "UYU"]

for currency in currencies:
  os.system(f'pprintjson {currency}.json -o {currency}-f.json')
  os.system(f'mv {currency}.json {currency}-s.json')
  os.system(f'mv {currency}-f.json {currency}.json')
  os.system(f'rm {currency}-s.json')
