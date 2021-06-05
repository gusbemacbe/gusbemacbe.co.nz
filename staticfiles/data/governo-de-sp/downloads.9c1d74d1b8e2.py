import io, json, requests, urllib, wget

days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
months = ["01", "02", "03", "04"]

path = "./"

for month in months:
  for day in days:
    print(f"https://www.saopaulo.sp.gov.br/wp-content/uploads/2021/{month}/2021{month}{day}_evolucao_aplicacao_doses.csv")
    
    # c = requests.get(f"https://www.saopaulo.sp.gov.br/wp-content/uploads/2021/{month}/2021{month}{day}_evolucao_aplicacao_doses.csv")
