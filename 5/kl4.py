class Car:
    """
    Klasa opisująca samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # pole prywatne, hermetyzacja

    def gaz(self):
        self.__predkosc += 10

    # enkapsulacja, wystawienie metod do odczytu wartości pól prywatnych
    def licznik(self):
        print(f"Jadę z szybkością {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    # metoda prywatna
    def __zmien_bieg(self):
        print("Zmiana biegu")


car = Car("Bentley", 2024)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)  # 50
# car.__predkosc = 0
car.licznik()  # Jadę z szybkością 50 km/h
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()
# Jadę z szybkością 50 km/h
# Jadę z szybkością 0 km/h
# Jadę z szybkością 50 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Jadę z szybkością 0 km/h
