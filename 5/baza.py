import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza została podłączona")
except sqlite3.Error as e:
    print("Błd podłączenia", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza została podłączona
# Połączenie zostało zamknięte