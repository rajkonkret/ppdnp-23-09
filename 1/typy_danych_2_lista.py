# kolekcje - wiele danych w jednym pudełku
# lista - przwechowuje wiele danych, różnego typu raz
# zachowuje kolejnosc przy dodawaniu elementów

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
