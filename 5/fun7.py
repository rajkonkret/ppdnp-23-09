def connect(**opcje):  # ** dowolna ilośc danych przelkazanych po nazwie, dane słownikowe
    print(opcje)


connect(a=9, b=10)  # {'a': 9, 'b': 10}
connect()
connect(name="Radek")


# {'a': 9, 'b': 10}
# {}
# {'name': 'Radek'}

def all_params(*args, **kwargs):
    print(args, kwargs)


all_params(1, 2, 3, 4, 5)
all_params(a=7, b=0, c=8, d=67)
# (1, 2, 3, 4, 5) {}
# () {'a': 7, 'b': 0, 'c': 8, 'd': 67}
all_params(1, 2, 3, 4, 5, a=8, b=8, name="Radek")
# (1, 2, 3, 4, 5) {'a': 8, 'b': 8, 'name': 'Radek'}
all_params()  # () {}
