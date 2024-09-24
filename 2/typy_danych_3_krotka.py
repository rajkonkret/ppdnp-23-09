# krotka (tupla) - kolekcja niemutowalna
# pozwala efektywniej zarządzać pamięcią
# PI = 3.14
# krotka jedoelementowe - zastępstwo stałych, zmiennej

tupla = ("Radek")
print(type(tupla))  # <class 'str'>

# tupla- dane oddzielone przecinkiem (moga byc w nawiasie ())
tupla_2 = "Raadek",
print(tupla_2)  # ('Raadek',), tupla jedoelementowa
print(type(tupla_2))  # <class 'tuple'>

# PEP8 zaleca by twworzyć tuple jednoelementową z nawiasami
tupla_3 = ("Raadek",)
print(type(tupla_3))  # <class 'tuple'>
print(tupla_3)  # ('Raadek',)

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla jest niemutowalna
# tupla_liczby[2] = 123  # TypeError: 'tuple' object does not support item assignment

# odczytanie elemntu z tupli
print(tupla_liczby[3])  # 11

# del tupla_liczby[3] # TypeError: 'tuple' object doesn't support item deletion
# można usunąc cala tuplę
del tupla_liczby
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined

tupla_imiona = "Radek", "Tomek", "Zenek", "Ania", "Ela", "Magda", "Iza", "Ewa"
print(tupla_imiona)
print(type(tupla_imiona))
# ('Radek', 'Tomek', 'Zenek', 'Ania', 'Ela', 'Magda', 'Iza', 'Ewa')
# <class 'tuple'>

print(tupla_imiona.index("Radek"))  # indeks numer 0
print(tupla_imiona.count("Iza"))  # Iza występuje 1 raz
# shift f6 - refactor->rename

# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>
a, b = 1, 2
print(a, b)  # 1 2
a, b = tup
print(a, b)

tup_2 = 1, 2, 3
# a, b = tup_2  # ValueError: too many values to unpack (expected 2)
a, *b = tup_2  # * worek na pozostałe dane
print(a, b)  # 1 [2, 3]
*a, b = tup_2
print(a, b)  # [1, 2] 3

print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Ania', 'Ela', 'Magda', 'Iza', 'Ewa')
# imie1, imie2, imie3
imie1, *imie2, imie3 = tupla_imiona
print(imie1, imie2, imie3)  # Radek ['Tomek', 'Zenek', 'Ania', 'Ela', 'Magda', 'Iza'] Ewa

imie1, imie2, *imie3 = tupla_imiona
print(imie1, imie2, imie3)  # Radek Tomek ['Zenek', 'Ania', 'Ela', 'Magda', 'Iza', 'Ewa']

# dostaniemy liste
print(sorted(tupla_imiona))  # ['Ania', 'Ela', 'Ewa', 'Iza', 'Magda', 'Radek', 'Tomek', 'Zenek']
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Ania', 'Ela', 'Magda', 'Iza', 'Ewa')

lista = list(tupla_imiona)
print(lista)
print(type(lista))
# ['Radek', 'Tomek', 'Zenek', 'Ania', 'Ela', 'Magda', 'Iza', 'Ewa']
# <class 'list'>
