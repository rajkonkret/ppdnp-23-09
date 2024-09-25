# pętle - dają nam możliwość wykonania wielokrotnie tego samego fragmentu (bloku) kodu
# for - pętla iteracyjna
import random
from itertools import zip_longest

for i in range(5):  # 0 .. 4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    print("Test podłoga")
    # print(_)

for i in range(20):
    print(i * 2)
    print(i + 20)

# przerobic lotto na petle
lista_kule = list(range(1, 50))
lista_wynik = []
for i in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)  # [4, 26, 29, 30, 3, 42]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

print(lista_wynik)  # [20, 11, 5, 14, 10, 43]
for c in lista_wynik:
    if c > 10:
        print("Większy od 10", c)
    else:
        print("Mniejsze od 10", c)
# Większy od 10 20
# Większy od 10 11
# Mniejsze od 10 5
# Większy od 10 14
# Mniejsze od 10 10
# Większy od 10 43

for i in range(0, 10, 2):  # (start, stop, krok)
    print(i)

for i in range(10, 0, -2):  # ujemny krok, odlicznie w dół
    print(i)
# 10
# 8
# 6
# 4
# 2
for i in range(-10, 0):
    print(i)

for c in lista3:  # # [0, 2, 4, 6, 8]
    if c == 2:
        c += 1  # c = c + 1
        print(c)
    print("Przy każdym przejściu pętli", c)
print("Poza pętlą")
# Przy każdym przejściu pętli 0
# 3
# Przy każdym przejściu pętli 3
# Przy każdym przejściu pętli 4
# Przy każdym przejściu pętli 6
# Przy każdym przejściu pętli 8

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
print(imiona)  # ['Radek', 'Tomek', 'Zenek', 'Ania']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania
# wypisać te elementy z indeksem 0 Radek
# sprawdzenie indeksu elementu
# print(lista.index("Mikołaj"))  # indeks numer 4
# lista.append("Mikołaj")
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):  # range(4) 0123
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - numeruje kolekcje i zwraca numerek i element
for p in enumerate(imiona):
    print(p)
    # (0, 'Radek')
    # (1, 'Tomek')
    # (2, 'Zenek')
    # (3, 'Ania') -> 3 Ania

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

ludzie = ['Radek', 'Tomek', 'Zenek', 'Magda']
wiek = [44, 55, 32, 27]
# wypisac to tak: Radek 44

for i in ludzie:
    print(i, wiek[ludzie.index(i)])
# Radek 44
# Tomek 55
# Zenek 32
# Magda 27
ludzie = ['Radek', 'Tomek', 'Zenek', 'Magda', "Ewa"]
wiek = [44, 55, 32, 27]
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-23-09\3\petle_zad1.py", line 144, in <module>
#     print(i, wiek[ludzie.index(i)])
#              ~~~~^^^^^^^^^^^^^^^^^
# IndexError: list index out of range

# zip() - łączy elementy wielu kolekcji
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Magda', 27)
for l, w in zip(ludzie, wiek):
    print(l, w)
# Radek 44
# Tomek 55
# Zenek 32
# Magda 27

# 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Zenek', 32))
# (3, ('Magda', 27))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d)  # Radek 44
print(a, c, d)  # 0 Radek 44
(a, (c, d)) = (3, ('Magda', 27))
print(a, c, d)  # 3 Magda 27
for i, (l, w) in enumerate(zip(ludzie, wiek)):
    print(i, l, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Magda 27

zip_list = zip_longest(ludzie, wiek, fillvalue=None)
print(zip_list)  # <itertools.zip_longest object at 0x000002640CB556C0> iterator, zwraca elementy po kolei
print("-----")
zipped = list(zip_list)
# for i in zip_list:
#     print(i)
# -----
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Magda', 27)
# ('Ewa', None)
#  iterator po przejsciu przez wszystkie elemnty kończy działanie
for i in zipped:
    print(i)
    # -----
    # ('Radek', 44)
    # ('Tomek', 55)
    # ('Zenek', 32)
    # ('Magda', 27)
    # ('Ewa', None)
for o, w in zipped:
    print(o, w)
# Tomek 55
# Zenek 32
# Magda 27
# Ewa None
