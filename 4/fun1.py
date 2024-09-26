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
    print(a + b)  # a, b zmienne lokalne


def odejmij(a, b, c=0):  # a,b - obowiązkowe, c ma wartośc domyślną
    print(a - b - c)


dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
# przekazywanie argumentów przez pozycje (argumenty pozycyjne)
dodaj2(5, 78)  # 83
print(a)  # a z góry
odejmij(1, 2)  # -1
odejmij(1, 2, 5)  # -6

# przekazywanie po nazwie (argumenty nazwane) keywords
odejmij(b=9, c=9, a=10)
odejmij(b=9, a=8)
dodaj2(b=9, a=34)

# mieszane, pozycyjne muszą być przed nazwanymi
odejmij(1, c=8, b=78)
odejmij(1, 8, c=78)

# odejmij(c=8, 1, 2)  # SyntaxError: positional argument follows keyword argument
# odejmij(a=1, 8, 78)  # SyntaxError: positional argument follows keyword argument
# odejmij(1, 8, a=78)  # TypeError: odejmij() got multiple values for argument 'a'

print(dodaj())
# 14
# None

# print(dodaj() + dodaj())  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# 14
