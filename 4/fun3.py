a = 10
b = 10


def dodaj():
    a = 8  # zmienne lokalne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # uzyje a globalnego
    a = 7
    b = 34
    print(a + b)


print(f"Zmienna a globalna (z góry) {a=}")  # Zmienna a globalna (z góry) a=10
dodaj()  # 16
print(f"Zmienna a globalna (z góry) {a=}")  # Zmienna a globalna (z góry) a=10
dodaj2()  # 20
print(f"Zmienna a globalna (z góry) {a=}")  # Zmienna a globalna (z góry) a=10
dodaj3()  # 41
# a globalne uległo zmianie
print(f"Zmienna a globalna (z góry) {a=}")  # Zmienna a globalna (z góry) a=7
dodaj2()  # bierza a i b globalne, 17
print(f"Zmienna a globalna (z góry) {a=}")  # Zmienna a globalna (z góry) a=7
