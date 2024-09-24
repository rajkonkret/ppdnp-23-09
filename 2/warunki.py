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
