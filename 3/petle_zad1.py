# pętle - dają nam możliwość wykonania wielokrotnie tego samego fragmentu (bloku) kodu
# for - pętla iteracyjna
import random

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
