from idlelib.iomenu import encoding

import chardet

# pip install chardet

with open('test.log', "r", encoding='utf-8') as f:
    raw_data = f.read()

print(raw_data)
# Nadpisane
# Dopisane
# Dopisane
# Dopisane
# Dodane
# Dośdane

# rb - odczyt bajtowy
with open('test.log', 'rb') as f:
    raw_data = f.read()

print(raw_data)
# b'Nadpisane\r\nDopisane\r\nDopisane\r\nDopisane\r\nDodane\r\nDo\xc5\x9bdane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6556784139655919, 'language': 'Turkish'}
# po dodaniu większej ilości polskich znaków do pliku
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
print(type(result))  # <class 'dict'>
encoding = result['encoding']
confidence = result['confidence']
print("Kodowanie znaków", encoding)  # Kodowanie znaków utf-8
print("Trafność", confidence)  # Trafność 0.99

print(raw_data.decode(encoding=encoding))
# Kodowanie znaków utf-8
# Nadpisane
# Dopisane
# Dopisane
# Dopisane
# Dodane
# Dośdane
# Dośćąźdane
