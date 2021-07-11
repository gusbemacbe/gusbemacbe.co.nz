from django.test import TestCase

# Create your tests here.
nz_adult_hour = 20
nz_trainee_hour = 16

def week(hour):
  week = hour * 40
  return week

def month(hour):
  month = week(hour) * 4
  return month

def year(hour):
  year = month(hour) * 12
  return year

def formatter(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', ' mil', ' milhões', ' bilhões', ' trilhões', 'quatrilhões', 'quintilhões', 'sextilhões', 'septilhões', 'octilhões', 'nonilhões', 'decilhões', ][magnitude])

print(week(nz_adult_hour))
print(week(nz_trainee_hour))

print(month(nz_adult_hour))
print(month(nz_trainee_hour))

print(formatter(year(nz_adult_hour)))
print(formatter(year(nz_trainee_hour)))

nz_minimum_developer_year = 50000
nz_average_developer_year = 65000
nz_maximium_developer_year = 95000

nz_minimum_developer_month = round(nz_minimum_developer_year / 12, 2)
nz_average_developer_month = round(nz_average_developer_year / 12, 2)
nz_maximium_developer_month = round(nz_maximium_developer_year / 12, 2)

nz_minimum_developer_week = round(nz_minimum_developer_month / 4, 2)
nz_average_developer_week = round(nz_average_developer_month / 4, 2)
nz_maximium_developer_week = round(nz_maximium_developer_month / 4, 2)

print(nz_minimum_developer_month)
print(nz_average_developer_month)
print(nz_maximium_developer_month)

print(nz_minimum_developer_week)
print(nz_average_developer_week)
print(nz_maximium_developer_week)