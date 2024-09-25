# wyjątki - błędy podczas wykonywania programu
# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-23-09\3\wyjatki.py", line 2, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

# do przechwycenia i obsługi wyjątków służy konstrukcja
# try except

try:
    # print(5 / 0)
    # print("a" + 9)
    print(int("A"))
    # raise KeyError("Brak klucza")  # rzucenie wyjątku (błedu)
    wynik = 90 / 33
except ZeroDivisionError:
    print("Nie dzielimy przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Błąd", e)
else:  # wykona się tylko gdy nie ma błedu
    print("Wynik działania", wynik)
finally:
    print("Wykona się zawsze")

print("Program nadal działa")
# Nie dzielimy przez zero
# Program nadal działa
# Bład typu
# Program nadal działa
# Błąd 'Brak klucza'
# Program nadal działa
# Wynik działania 2.727272727272727
# Program nadal działa
# Wynik działania 2.727272727272727
# Wykona się zawsze
# Program nadal działa
# Bład wartości
# Wykona się zawsze
# Program nadal działa

# try except [else - finally]
