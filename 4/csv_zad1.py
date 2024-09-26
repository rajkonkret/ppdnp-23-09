# pliki csv - dane w pliku oddzielone znakiem podziału
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['Radek', 'Coe', 2, '9.1']

dictionary = dict(zip(fields, row))
filename = 'records.csv'

print(dictionary)  # {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'}

with open(filename, 'w', newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = 'records_2.csv'
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dictionary)

products = [
    {"sku": 1, 'exp_date': "today", 'price': 200},
    {"sku": 2, 'exp_date': "today", 'price': 50},
    {"sku": 3, 'exp_date': "tomorrow", 'price': 100},
    {"sku": 4, 'exp_date': "today", 'price': 700},
]

discount_fields = ["sku", "exp_date", "price"]

filename = 'records_3_discount.csv'
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=discount_fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)  # writerows

# newline="" - ominięcie problemu podwójnych enterów
# delimiter=";" - znak podziału
