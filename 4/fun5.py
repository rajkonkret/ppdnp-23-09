# stworzyc funkcję kantor
# ma posiadać dwie funkcje wewnętrzne usd, eur
# w zależnosci od parametru ma zwracać wybraną funkcję ( adres funkcji)
# użyc tych funkcje do przeliczenia waluty
# dodać możliwosć przekazania dowolnej kwoty
def kantor(waluta):
    def usd(kwota=0):
        print(f"Przeliczam dolary {kwota} na {kwota * 3.90} pln")

    def eur(kwota=0):
        print(f"Przeliczam euro {kwota} na {kwota * 4.30} pln")

    if waluta == "eur":
        return eur
    else:
        return usd


kantor_usd = kantor("usd")
kantor_usd()

kantor_eur = kantor("eur")
kantor_eur()
# Przeliczam dolary 0 na 0.0 pln
# Przeliczam euro 0 na 0.0 pln

kantor_eur(1000)  # Przeliczam euro 1000 na 4300.0 pln
kantor_usd(5678)  # Przeliczam dolary 5678 na 22144.2 pln
