# klasa - element programowania obiektowego
# klasa - szablon, przepis
# wskazuje cechy i funkcje obiektu
# cechy - zmienne
# funkcje - metody
# definicja klasy nie uruchamia klasy
# budowanie obiektu klasy uruchamia elemnty klasy
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja


# deklaracja klasy
# PEP8 zaleca by nazwy klas pisac dużą literą PamelCase
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"


print(Human.__doc__)
#     Klasa Human opisująca człowieka w pythonie
print(print.__doc__)

# tworzenie obiektu klasy Human
cz1 = Human()
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
cz1.plec = "k"
cz1.wiek = 45
cz1.imie = "Ania"
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
# k
# 45
# Ania
cz2 = Human()
cz2.plec = "m"
cz2.wiek = 39
cz2.imie = "Radek"
print(cz2.plec)
print(cz2.wiek)
print(cz2.imie)
# m
# 39
# Radek
