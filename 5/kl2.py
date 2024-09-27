class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wzrost = wzrost
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        print("Nazywam się", self.imie)

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłęm w drogę")


cz1 = Human("radek", 56, 190, "m")
print(cz1.wzrost)
cz1.powitanie()
# 190
# Nazywam się radek
cz1.wypisz_wzrost()
cz1.ruszaj()
cz2 = Human("ania", 56, 170)
cz2.ruszaj()
# Ruszyłęm w drogę
# Ruszyłam w drogę