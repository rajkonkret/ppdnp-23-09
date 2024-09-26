# działania z plikami
# context manager
# with - context manager w pythonie
# open() - praca z plikami
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler - rura do pliku
    fh.write("Powitanie\n")
    fh.write("Powitanie\n")
    # \n - znak konca lini, w pliku linia ma długosc 80 i nie jest automatycznie ten znak dodawany
    fh.write("Kolejne\n")

# "x" - tworzy nowy plik, gdy plik nie istnieje
# gdy istnieje mamy bład
# with open('test.log', 'x', encoding='utf-8') as file:
#     file.write("Coś\n")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-23-09\4\pliki_zad1.py", line 23, in <module>
#     with open('test.log', 'x') as file:
#          ^^^^^^^^^^^^^^^^^^^^^
# FileExistsError: [Errno 17] File exists: 'test.log'

# "w" - kasuje plik i tworzy nowy plik o tej nazwie
with open('test.log', 'w', encoding='utf-8') as f:
    f.write("Nadpisane\n")

with open('test.log', "a", encoding='utf-8') as f:
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dodane\n")
    f.write("Dośdane\n")
    f.write("Dośćąźdane\n")

with open('test.log', "r", encoding='utf-8') as file:
    lines = file.read()  # odczyt danych z pliku

print(lines)
# Nadpisane
# Dopisane
# Dopisane
# Dopisane
# Dodane
