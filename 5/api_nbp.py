import requests

# pip install requests

url = 'https://api.nbp.pl/api/exchangerates/rates/A/USD/'
# http get

response = requests.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx warning, przekierowania itd
# 4xx bład, po stronie uzytkownika, 404 - błedny url, 400 Bad Request błędny parametr
# 5xx błedy po stronie serwera 500 Internal Server Error

print(response.text)
print(type(response.text))  # <class 'str'>

data = response.json()  # zamian jsona na słownik
print(data)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '189/A/NBP/2024', 'effectiveDate': '2024-09-27', 'mid': 3.8368}]}
print(data['code'])  # USD
print(data['rates'][0]['mid'])  # 3.8368
