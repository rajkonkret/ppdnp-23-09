user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # <class 'float'>
print(type(wersja))  # <class 'float'> zmiennoprzecinkowe
liczba = 456123789456  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# print("Witaj %s, masz teraz %d lat." % (wiek, user))# TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit
print("Witaj %(user)s, masz teraz %(wiek)d lat." % {'user': user, 'wiek': wiek})
print("Witaj %(user)s, masz teraz %(age)d lat." % {'user': user, 'age': wiek})
print("Witaj %(user)s, jesteś %(user)s." % {'user': user})
# Witaj Tomek, masz teraz 39 lat.
# Witaj Tomek, jesteś Tomek.

print("Witaj {}, masz terz {} lat".format(user, wiek))  # Witaj Tomek, masz terz 39 lat

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
print("Używamy wersji pythona %f" % 3.9)  # Używamy wersji pythona 3.900000
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4
# zaokrągla przy wyświetlaniu
print("Wynik= %.2f" % 3.8769)  # Wynik= 3.88
x = 3.14
print("Zero miejsc po przecinku %.f" % x)  # Zero miejsc po przecinku 3
print("X nadal się nie zmieniło", x)  # X nadal się nie zmieniło 3.14

# zaokraglanie liczb
y = round(x)
print("x=", x, "y=", y)  # x= 3.14 y= 3
x = 3.1416
print(round(x, 2))  # 3.14

print(f"Uzywamy wersji python{wersja}")  # Uzywamy wersji python3.900001
print(f"Uzywamy wersji python{wersja:.1f}")  # Uzywamy wersji python3.9
print(f"Uzywamy wersji python{wersja:.2f}")  # Uzywamy wersji python3.90
print(f"Uzywamy wersji python{wersja:.0f}")  # Uzywamy wersji python4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^25}")  # "          Tomek          "

print(liczba)  # 456123789456
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 456,123,789,456
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 456_123_789_456
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 456.123.789.456
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 456 123 789 456

liczba2 = 15000000
liczba_2 = 15_000_000
print(type(liczba_2))  # <class 'int'>
print(liczba_2)  # 15000000
