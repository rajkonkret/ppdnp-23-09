import random
from random import randrange

print(random)
# <module 'random' from 'C:\\Users\\CSComarch\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\random.py'>
# import - załaduj do pamięci
# biblioteka do działań na liczbach pseudolosowych

print(random.randint(1, 100))  # int OD 1 DO 100 włącznie
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4
print(random.random())  # 0.43805158771693975 float od 0 do 0,99999999
print(random.random() * 10)  # 8.770667065459348 float od 0 do 9,99999999

lista = [67, 45, 32, 68, 89, 90, 42]
print(random.choice(lista))  # wylosował element 42

# maszyna losujaca
# beben z kulami
# losujemy kule, wyn = random.choice(lista_kule)
# wyciagamy kule, lista_kule.remove(wyn)
# pokazujemy kule, print(wyn)
lista_kule = list(range(1, 50))  # losuje od 1 do 49
print(lista_kule)

wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # losuje powtarzające sie numery [47, 46, 15, 17, 25, 46]
print(random.sample(lista_kule, k=6))  # losuje bez powtórzen [18, 14, 25, 5, 19, 16]
print(random.sample(lista_kule, 6))  # [5, 38, 24, 47, 29, 34]
