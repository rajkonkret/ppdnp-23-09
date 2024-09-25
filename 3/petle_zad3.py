#  while - pętla sterowana warunkiem

# kończy się gdy warunk jest False
# pętla nieskończona

# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerywa pętle
#
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!

print(licznik)  # 11
licznik = 0

while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!

# password = input("Podaj hasło")
# while password != 'secret':
#     password = input("Błędne hasło, podaj ponownie")
#
# print("Hasło prawidłowe")
# Błędne hasło, podaj ponownieadasfsdv
# Błędne hasło, podaj ponowniewqee
# Błędne hasło, podaj ponowniesecret
# Hasło prawidłowe

# lista = []
# lista_int = []
# while True:
#     wej = input("Podaj liczbę")  # str
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
# # A string is numeric if all characters in the string are numeric
# print(lista)  # ['1', '2', '3', '4', '5', '6', '7', '8', '45', '67', '90', '785453']
# print(lista_int)
# # ['5', '6', '78']
# # [5, 6, 78]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

# od pythona 3.7 zachowuje kolejność w słowniku
print(my_list)
# [1, 2, 3, 4, 6]
my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))  # {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}
unique_numbers = list(dict.fromkeys(my_list))
print(unique_numbers)  # [1, 5, 2, 3, 4, 6]
