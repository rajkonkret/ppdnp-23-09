# funkcja lambda
# skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa, możliwość użycia w miejscu deklaracji

def odejmij(a, b):
    return a - b


print(odejmij(8, 9))

odejmij2 = lambda a, b: a - b
print(odejmij2(8, 6))  # 2

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))
print(wiek(10))
print(wiek(17))
print(wiek(18))
print(wiek(25))
# dziecko
# nastolatek
# nastolatek
# dorosły
# dorosły

# mapowanie
lista = [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]
lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)
print(lista_wyn)
# [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]


def zmien(x):
    return x * 2


lista_wyn2 = []
for i in lista:
    lista_wyn2.append(zmien(i))
print(lista_wyn2)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

# funkcje wyższego rzedu
# map() - pobiera element z kolekcji, wykonuje na nim zadaną funkcję
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

# lambda jako funkcja anonimowa
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
# Zastosowanie map(): [4, 8, 12, 40, 80, 200, 280, 800, 1200, 2000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 12, lista))}")
print(f"Zastosowanie map(): {(map(lambda x: x * 12, lista))}")  # Zastosowanie map(): <map object at 0x000001E42C84E8F0>
# Zastosowanie map(): [12, 24, 36, 120, 240, 600, 840, 2400, 3600, 6000]

# filtrowanie danych
print(lista)  # [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]
l3 = []
for i in lista:
    if i < 20:
        l3.append(i)
print(l3)  # [1, 2, 3, 10]

# filter() - zwraca elemnty spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 20, lista))}")
# Zastosowanie filter(): [1, 2, 3, 10]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3, lista))}")
# Zastosowanie filter(): [10, 20, 50, 70, 200, 300, 500]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 100, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 100, lista))}")
# Zastosowanie filter(): [10, 20, 50, 70]
# Zastosowanie filter(): [10, 20, 50, 70]
