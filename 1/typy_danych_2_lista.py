# kolekcje - wiele danych w jednym pudełku
# lista - przwechowuje wiele danych, różnego typu raz
# zachowuje kolejnosc przy dodawaniu elementów
from time import perf_counter

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(type(pusta_lista))  # <class 'list'>
print(pusta_lista)  # []

# append()
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Magda")
lista.append("Ewa")
lista.append("Ela")
lista.append("Iza")
lista.append("Mariusz")
lista.append("Przemek")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Magda', 'Ewa', 'Ela', 'Iza', 'Mariusz', 'Przemek']
#     0        1         2        3      4      5      6         7         8
#     -9       -8        -7       -6     -5     -4    -3        -2        -1
print(len(lista))  # długośc 9
print(lista[0])  # Radek
print(lista[5])  # Ela
print(lista[7])  # Mariusz

# print(lista[10])  # IndexError: list index out of range
print(lista[8])  # Przemek
print(lista[len(lista) - 1])  # Przemek
print(lista[-1])  # Przemek
print(lista[-2])  # Mariusz
print(lista[-3])  # Iza

# wyświetlanie fragmentu listy (slicowanie)
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'], indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Magda', 'Ewa', 'Ela', 'Iza', 'Mariusz', 'Przemek']
print(lista[2:8])  # ['Zenek', 'Magda', 'Ewa', 'Ela', 'Iza', 'Mariusz']
print(lista[2:15])  # ['Zenek', 'Magda', 'Ewa', 'Ela', 'Iza', 'Mariusz', 'Przemek'], nie ma błedu, okaże do ostatniego
print(lista[2:6])  # indeksy 2,3,4,5 -> ['Zenek', 'Magda', 'Ewa', 'Ela']
print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Magda', 'Ewa', 'Ela', 'Iza', 'Mariusz', 'Przemek']
print(lista[2:3])  # ['Zenek']
print(lista[2:2])  # []
print(lista[10:29])  # [], nie będzie błedu

# ['Radek', 'Tomek', 'Zenek', 'Magda', 'Ewa', 'Ela', 'Iza', 'Mariusz', 'Przemek']
#     0        1         2        3      4      5      6         7         8
#     -9       -8        -7       -6     -5     -4    -3        -2        -1

print(lista[-2:0])  # [] -> [7:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek', 'Magda', 'Ewa', 'Ela', 'Iza'] -> [0:7]

# lista_15 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
lista_15 = list(range(15))  # od 0 do 14, domyślnie początek jest 0
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:15:2])  # [start:stop:step]
print(lista_15[0::2])  # [start:stop:step]
# [0, 2, 4, 6, 8, 10, 12, 14]
# [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]

# nadpisanie elementu w liście
# zmieniana jest bazowa lista
lista[3] = "Mikołaj"
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Mikołaj', 'Ewa', 'Ela', 'Iza', 'Mariusz', 'Przemek']

# insert() - wstawienie lementu na wskazanym indeksie
lista.insert(1, "Karol")
print(lista)
# ['Radek', 'Karol', 'Tomek', 'Zenek', 'Mikołaj', 'Ewa', 'Ela', 'Iza', 'Mariusz', 'Przemek']

# sprawdzenie indeksu elementu
print(lista.index("Mikołaj"))  # indeks numer 4
lista.append("Mikołaj")
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Mikołaj', 'Ewa', 'Ela', 'Iza', 'Mariusz', 'Przemek', 'Mikołaj']
print(lista.index("Mikołaj"))  # 4 - podaje pierwsze wystąpienie

# usunięcie po elemencie, pierwszy z listy
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Ewa', 'Ela', 'Iza', 'Mariusz', 'Przemek', 'Mikołaj']

# usunięcie po indeksie, zwraca usunięty element
print(lista.pop(5))  # Ela
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Ewa', 'Iza', 'Mariusz', 'Przemek', 'Mikołaj']
print(lista.pop(-2))  # Przemek
print(lista.pop())  # Mikołaj, usunie ostatni element z listy

a = 1
b = 3
a = b
print(a, b)  # 3 3
b = 7
print(a, b)  # 3 7
#   a   =   b
lista_2 = lista  # a = b, kopiowany jest adres listy, referencja
print(lista_2)
print(lista)
lista_copy = lista.copy()  # kopia elementów listy
# ['Radek', 'Karol', 'Tomek', 'Zenek', 'Ewa', 'Iza', 'Mariusz']
# ['Radek', 'Karol', 'Tomek', 'Zenek', 'Ewa', 'Iza', 'Mariusz']
lista.clear()  # usnięcie wszystkich elementów listy, b = 7
# print(a, b)
print(lista_2)  # []
print(lista)  # []
print(lista_copy)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Ewa', 'Iza', 'Mariusz']
# []
# []
print(id(lista_2))  # 2589967389056
print(id(lista))  # 2589967389056
print(id(lista_copy))  # 2113999798080

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

liczby = [54, 999, 34, 22, 12.34, 687, "A"]
print(liczby)  # liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
# liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
# kod ascii
print(ord("A"))  # kod 65
print(ord("1"))  # kod 49

lista_osob = ['radek', 'ola', 'lena', 'agata']
lista_osob.sort()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']

lista_osob.sort(reverse=True)  # sortuje i odwraca
print(lista_osob)  # ['radek', 'ola', 'lena', 'agata']

lista_osob.reverse()  # tylko odwraca, zmienia listę
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']

print(lista_osob[::-1])  # ['radek', 'ola', 'lena', 'agata'], odwraca wypisanie, nie zmienia listy
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']

liczby[3] = 666
print(liczby[0:3])
print(liczby[-2])
print(liczby)  # [54, 999, 34, 666, 12.34, 687, 'A']

del liczby  # usunięcie listy z pamięci
# print(liczby)  # NameError: name 'liczby' is not defined

# rozpakowanie sekwencji
tekst = "Pyth on."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

krotka = tuple(lista_copy)  # tuple() - rzutowanie(zamiana) na krotkę, tuplę
print(type(krotka))
print(krotka)  # ('Radek', 'Karol', 'Tomek', 'Zenek', 'Ewa', 'Iza', 'Mariusz')
