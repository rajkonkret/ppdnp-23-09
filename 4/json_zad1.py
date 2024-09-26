# json - {"name":"John", "age":30, "car":null}
# dane typu klucz wartość
# uzywany do komunikacji pomiędzy sytemami w internecie
# w pythone dane json zamieniamy na slownik
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)

# upiększony
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4)

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as f:
    data = json.load(f)

print(data)
print(type(data))
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>
print(data['name'])  # Radek

# zamiana słownika na json
json_text = json.dumps(data)
print(type(json_text))
print(json_text)
# <class 'str'>
# {"age": 40, "czy_pali": null, "name": "Radek"}

# wczytanie jsona jako słownik
dict_json = json.loads(json_text)
print(dict_json)
print(type(dict_json))
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>
