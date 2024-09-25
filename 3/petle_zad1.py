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
