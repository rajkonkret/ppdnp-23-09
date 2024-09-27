from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        metoda inicjalizujaca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę zszybkością", self.szybkosc)

    # metoda abstrakcyjna
    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko k o ko")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("Kier kir kir kier")


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzel", 50)
# or1.latam()  # Tu Orzel Lecę zszybkością 50
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę zszybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam
kur2.wydaj_odglos()
or2 = Orzel("Orzel Bielik", 50)
or2.latam()
or2.wydaj_odglos()
# Tu Kura domowa Ja nie latam
# Ko ko ko k o ko
# Tu Orzel Bielik Lecę zszybkością 50
# Kier kir kir kier

# polimorfizm - obiekty róznych klas mają wspólne cechy
lista = [or2, kur2]
for i in lista:
    i.wydaj_odglos()
# Kier kir kir kier
# Ko ko ko k o ko
