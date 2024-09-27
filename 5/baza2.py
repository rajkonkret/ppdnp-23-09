import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza została podłączona")

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    """

    insert = """
    INSERT INTO developers (id,name,email,salary) VALUES (1,'Radek','radek@radek.pl','10000');
    """

    # c.execute(query)
    # conn.commit()

    c.execute(insert)
    conn.commit()
except sqlite3.Error as e:
    print("Błd podłączenia", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza została podłączona
# Połączenie zostało zamknięte
