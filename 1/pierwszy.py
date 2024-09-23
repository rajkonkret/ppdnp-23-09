import sys

print()  # wypisz/wydrukuj

print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
# ctrl d - powielanie linijki
print('Nazywam się Radek')  # Nazywam się Radek
# print('Nazywam się Radek")  # Nazywam się Radek
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-23-09\1\pierwszy.py", line 9
#     print('Nazywam się Radek")  # Nazywam się Radek
#           ^
# SyntaxError: unterminated string literal (detected at line 9)
# ctrl / - komentowanie zaznaczonego kodu
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'
# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'> dane tekstowe, string
print("39")  # 39, str
print(39)  # 39
print(type(39))  # <class 'int'>, liczby całkowite, integer

print("39" + "39")  # 3939, konkatenacja, łaczennie tekstów
print(39 + 39)  # operacja na liczbach, wynik 78
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str, silne typowanie
print(int("39") + 39)  # 78 int() - rzutowanie na liczbę
# print(int("A"))  # ValueError: invalid literal for int() with base 10: 'A'

print("39" + str(39))  # str() - zamiana na tekst, string

print(8 + 8 + 8)
print("8" + "8" + "8")

print(5 * "4")  # 44444
print(160 * 22)  # 3520
print("160" * 22)  # 160160160160160160160160160160160160160160160160160160160160160160

# zmienna - pudełko na dane
# typowanie dynamiczne
# typ jest określny na podstawie zawartości pudełka
# przechowuje jeden element
# snake_case
# nazwa zmiennej powinna sugerować co zawiera zmienna
liczba = 39
print(liczba)

liczba = "39"
print(liczba)
print(type(liczba))  # <class 'str'>

name = "Radek"
print(type(name))
print(name + " Kowalski")  # RadekKowalski, Radek Kowalski

name = 90
# print(name + "Kowalski")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# podpowiedź typów, (nie jest to ustawienie typu)
name: str = "Radek"
print(name)
print(type(name))
name = 90
print(name)
# Radek
# <class 'str'>
# 90

age = 56
print(age)
print(type(age))
# 56
# <class 'int'>
