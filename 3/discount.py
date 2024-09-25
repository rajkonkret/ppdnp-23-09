from datetime import datetime, date, timedelta

today = date.today()
print(today)  # 2024-09-25

print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas", time)  # Aktualny czas 2024-09-25 15:22:35.335948

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-09-26

print(time.time())
print(today.day)
# 15:29:31.788414
# 25

formatted_data = datetime.now().strftime("%d/%m/%Y")
print(formatted_data)  # 25/09/2024

formatted_time = datetime.now().strftime("%H:%M")  # %H - 24h
print(formatted_time)  # 15:37

# jak zrobic date w formacie amerykańskim 11:23 am
formatted_time_usa = datetime.now().strftime("%I:%M %p")  # %I 12 h
print(formatted_time_usa)  # 03:42 PM

products = [
    {"sku": 1, 'exp_date': today, 'price': 200},
    {"sku": 2, 'exp_date': today, 'price': 50},
    {"sku": 3, 'exp_date': tomorrow, 'price': 100},
    {"sku": 4, 'exp_date': today, 'price': 700},
]

print(products)
for p in products:
    # print(p)  # {'sku': 4, 'exp_date': datetime.date(2024, 9, 25), 'price': 700}
    # print(p['exp_date'])
    if p['exp_date'] != today:
        continue  # wróć na początek petli, bierze kolejny element
    p['price'] *= 0.8  # p = p * 0.8 obniżka o 20%
    print(f"""Price for sku {p['sku']}
is now {p['price']}""")
# Price for sku 1
# is now 160.0
# Price for sku 2
# is now 40.0
# Price for sku 4
# is now 560.0
