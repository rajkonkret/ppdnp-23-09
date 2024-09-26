import csv

fields = []
rows = []

# filename = 'records.csv'
filename = 'records_3_discount.csv'

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # ;
    # StopIteration - wyczerpalismy dane
    csv_f.seek(0)  # ustawiamy odczyt na początek pliku
    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x000001982EF057E0>
    fields = next(csvreader)  # odczytuje pojedynczy element i ustawia wskażnik na następny, odczyta indeks 0
    for row in csvreader:  # wystartuje od drugiego elementu kolekcji (indeks 1)
        # print(row)
        rows.append(row)
# ['name', 'branch', 'year', 'cgpa']
# ['Radek', 'Coe', '2', '9.1']

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['Radek', 'Coe', '2', '9.1']]
# Fields: ['sku;exp_date;price']
# Rows: [['1;today;200'], ['2;today;50'], ['3;tomorrow;100'], ['4;today;700']]
# po ustawieniu delimiter=";"
# Fields: ['sku', 'exp_date', 'price']
# Rows: [['1', 'today', '200'], ['2', 'today', '50'], ['3', 'tomorrow', '100'], ['4', 'today', '700']]
