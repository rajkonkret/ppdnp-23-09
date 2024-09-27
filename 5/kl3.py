class Pojazd:
    """
    klasa Pojazd
    """

    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("Kolor:", self.kolor)


class Samochod(Pojazd):  # Dziedziczymy po klasie Pojazd

    def __init__(self, kolor, marka):
        super().__init__(kolor)  # musimy wywołąć konstruktor klasy wyższej
        self.marka = marka

    def info(self):
        print("Marka:", self.marka)
        super().info()  # super() - klasa wyższa, u nas Pojazd


poj = Pojazd("czerwony")
poj.info()

sam = Samochod("zielony", "Bentley")
sam.info()
# Kolor: czerwony
# Marka: Bentley
# Kolor: zielony
