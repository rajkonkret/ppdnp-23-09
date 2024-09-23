from gettext import textdomain

tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# #3 Witaj Świecie
# <class 'str'>

# teksty są niemutowalne, nie zmieniamy oryginalnego tekstu. dostajemy kopie tekstu
tekst.upper()
print(tekst)  # " Witaj Świecie"
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE

# zamiana na małe litery
print(tekst.lower())  # witaj świecie

print(tekst)
# Witaj Świecie
# 0123456789...

print(tekst.index("j"))  # indeks numer 4, pozycja 5
print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # 0, indeksy 0123

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

tekst_zamiana = "Witaj Dobry Świecie"
print(tekst_zamiana.replace("Dobry", ""))  # Witaj  Świecie
print(tekst.removesuffix(
    "Świecie").strip())  # "Witaj", strip() - usunie białe znaki, spacje tabulatory itd na początku i nakońcu

print(tekst[4])  # "j" - litera na 4 indeksie (pozycja 5)
encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # b'Witaj \xc5\x9awiecie'
# b - dane typu bajtowego
# \xc5\x9 - szesnastkowa wartosc bajtów
# \xc5 - 197 dziesietnie
print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
# f - fstring, formatowanie tektu
tekst_format = f"Mam na imię {imie} i lubię pythona"
print(tekst_format)  # Mam na imię Radek i lubię pythona

tekst_format1 = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format1)
# "	Mam na imię Radek
# i lubię pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"  # %s - string
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!

print("Witaj", imie)  # Witaj Radek

# tekst wielolinijkowy
print("""Tekst
    wielolinijkowy""")
#  "Tekst
#     wielolinijkowy"
