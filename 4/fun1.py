# funkcje - wydzielony fragment kodu, można go wywołąć w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# w miejscu deklaracji funkcja nic nie wykonuje
# zeby wykonac funkcje nalzy ją wywołać

a = 6
b = 8


# definicja funkcji
# tu się nic nie wykona
def dodaj():  # funkcja nie ma argumentów
    print(a + b)


def dodaj2(a, b):  # a, b - dwa obowiązkowe argumenty
    print(a + b)  # a,b zmienne lokalne


dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 78)  # 83
