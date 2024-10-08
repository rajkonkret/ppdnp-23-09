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
# tekst = input("Podaj imię")  # zwraca strmi
# print(tekst)
# print(type(tekst))  # <class 'str'>

# napisac aplikacje kalkulator
# pobrac dwie liczby
# wyswietlic wynik (+)
a = input("Podaj pierwszą liczbę")
b = int(input("Podaj drugą liczbę"))
print(float(a) + b)  # 11.0

# napisac aplikację słownik pol-ang z wykoryzstaniem słownika
# słownik
# wypisac klucze
# pobrac słowko, które chce przetłumaczyc
# wypisać tłumaczenie
pol_ang = {'kot': 'cat', 'pies': 'dog', 'dach': 'roof'}
print("Znam takie słówka", pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia")
# print(pol_ang[odp.lower().strip()])
print(pol_ang.get(odp, "nie mo"))
# print(f"Tłumaczone słowo {pol_ang[odp.lower().strip()]}")
print(f"Tłumaczenie dla słowa: {odp} - {pol_ang.get(odp, "nie mo")}")
# Znam takie słówka dict_keys(['kot', 'pies', 'dach'])
# Podaj słówko do przetłumaczenia>? kot
# cat
# Tłumaczone słowo cat
# Tłumaczenie dla słowa: kot - cat
