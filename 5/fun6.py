# stworzyc funkcję obliczającą średnią
def liczby(name=None, *cyfry):  # moze przyjąc dowolną ilosc elementów przekazanych po pozycji
    print(cyfry)
    count = len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count

    except Exception as e:
        print("Błąd", e)
    else:
        print(f"Srednia dla ucznia {name} wynosi", avg)
    finally:
        print("Oblicznia zakończone")


liczby("Radek", 6, 6, 6, 6, 6, 6, 6, 6, 6)
liczby()
liczby(1, 2, 3)
liczby(1, 2, 31, 2, 3, 4, 5)
# ()
# (1, 2, 3)
# (1, 2, 31, 2, 3, 4, 5)
# ()
# Błąd division by zero
# Oblicznia zakończone
# (1, 2, 3)
# Srednia wynosi 2.0
# Oblicznia zakończone
# (1, 2, 31, 2, 3, 4, 5)
# Srednia wynosi 6.857142857142857
# Oblicznia zakończone
# (6, 6, 6, 6, 6, 6, 6, 6, 6)
# Srednia dla ucznia Radek wynosi 6.0
# Oblicznia zakończone
# ()
# Błąd division by zero
# Oblicznia zakończone
# (2, 3)
# Srednia dla ucznia 1 wynosi 2.5
# Oblicznia zakończone
# (2, 31, 2, 3, 4, 5)
# Srednia dla ucznia 1 wynosi 7.833333333333333
# Oblicznia zakończone
