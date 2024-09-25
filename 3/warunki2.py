# od Pythona 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().strip():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam Javę")
    case _:  # wartość domyślna
        print("Nie znam takiego języka")

print(lista)
# ['Znam Javę']
# match case jest idealny gdy mamy konkretne warunki np: czy rowne java itd
# if idelany do przeziałów n.: od 10000 do 29999
