# instrukcje warunkowe -
# instrukcje sterowania przepływem programu
# w zależności od warunku (True lub False) wykona jeden lub drugi blok programu
# warunek musi zwracac bool
# if
odp = True
print(bool(odp))  # True
odp = False
if odp:
    # blok wykonywany gdy warunek spełniony, wcięcie 4 spacje
    #  print("")# IndentationError: unindent does not match any outer indentation level
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")

odp = "Radek"
print(bool(odp))
if odp:
    print("Radek")  # Radek

if odp == "Radek":  # == porównanie, wynik porównania jest bool
    print('Nadal Radek')  # Nadal Radek

if odp == "Tomek":
    print("Tomek")
else:  # w przeciwnym razie
    print('To nie jest Tomek')  # To nie jest Tomek

a = "Radek"
if len(a) > 3:
    print(f"Długość wynosi więcej niż 3, {len(a)}")

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długość wynosi więcej niż 3, {n}")
# Długość wynosi więcej niż 3, 5
# Długość wynosi więcej niż 3, 5

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długość wynosi więcej niż 3, {n}")
# n:= zastepuje te dwie komendy
# n = len(a)
# if n > 3:

# kolejnośc ma znaczenie
# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 30_000:  # kolejny warunek
#     podatek = 0.2
# elif zarobki < 100_000:  # kolejny warunek
#     podatek = 0.4
# else:  # pozostałe przypadki
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki}")
# dodac podatek 0.2 dla dochodów od 10000 do 29999
# Podaj zarobki29999
# Podatek wynosi 5999.8

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")  # Rabat wynosi 25
rabat = 25 if suma_zam > 100 else 0  # jak warunek spełniony to co po prawej trafia do zmiennej rabat
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# zasymulujemy system zbierania logów
# zmienne będą przechować dane z jakiego systemu przyszły logi
# email, console, inny (else)
# dla console: "Stało się coś strasznego"
# dla email: "System email"
# w zmiennej error bedzie poziom błedu
# error, medium, inny
# gdy system email dopisz do listy błedów opis poziomu błedu jaki przyszedł do nas
alert_system = 'email'
error = 'error'
lista_b = []

if alert_system == 'console':
    print("Stało się coś strasznego")
elif alert_system == 'email':
    print("System email")
    if error == 'error':
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inny")
else:
    print("Inny system")

print(lista_b)  # ['Krytyczny']

a = 10
assert a > 5
# assert a > 15 # AssertionError
assert 'Krytyczny' in lista_b
# assert 'Ostrzeżenie' in lista_b # AssertionError

# napisać test z...
# zadać pytanie
# pobrac odpowiedź
# sprawdzic odpowiedź
# wypisać wynik
punkty = 0
odp = input("Podaj rok Chrztu Polski")
if odp == '966':
    print("Brawo")
    punkty += 1  # punkty = punkty + 1
else:
    print("Bład")
print(punkty)
odp = input("Podaj rok Bitwy pod Grunwaldem")
if odp == '1410':
    print("Brawo")
    punkty += 1  # punkty = punkty + 1
else:
    print("Bład")
print(punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
a = 1
a *= 2  # a = a * 2
print(a)  # 2
a += 3  # a= a + 3
print(a)  # 5
