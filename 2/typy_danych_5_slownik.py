# słownik - para klucz-wartość
# {'user':'Radek', 'wiek':78}
# słownik jest odpowiednikiem jsona
# { "firstName": "John", "lastName" : "Smith"}
# klucze nie mogą się powtarzać

# pusty słownik
dictionary = dict()
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

dictionary_1 = {}
print(type(dictionary_1))  # <class 'dict'>
print(dictionary_1)  # {}

# dodawanie elemntu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary["wiek"] = 38
print(dictionary)  # {'imie': 'Radek', 'wiek': 38}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 38])
# dict_items([('imie', 'Radek'), ('wiek', 38)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek
# print(dictionary['Imie'])  # KeyError: 'Imie'

print(dictionary.get("Imie"))  # None, Process finished with exit code 0
print(dictionary.get("Imie", "Domyślna"))  # Domyślna

dictionary.update({'data': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38, 'data': '12-12-2024'}

dict_small = {'x': 2}
print(dict_small)  # {'x': 2}
dict_small.update([('y', 3), ('z', 5)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 5}

# input() - pobieranie danych od użytkownika
tekst = input("Podaj imię")
print(tekst)
print(type(tekst))# <class 'str'>