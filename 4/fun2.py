# funkcje zwracające wynik
# kończą się instrukcją return

def dodaj(a, b):
    return a + b  # return, zwróc wynik


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(6, 23))  # 29
wynik = dodaj(67, 89)
print("Wynik działania", wynik)  # Wynik działania 156
a = 8
b = 9
print(dodaj(a, b))  # 17
print(odejmij())
print(odejmij(1))
print(odejmij(11, 2))
print(odejmij(11, 21, 2))
# 0
# 1
# 9
# -12
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, cena=5000))
# 1230.0
# 1080.0
# 5750.0

zm = oblicz_vat(1000)
print(type(zm))  # <class 'float'>
if zm == 1230:
    print("Ok")  # Ok

print(dodaj(6, 89) + odejmij(234, 67, 22))  # 240
