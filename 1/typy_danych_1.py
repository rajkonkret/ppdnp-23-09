import sys

wiek = 47
rok = 2024
temp = 36.6

print(temp)
print(type(temp))
# 36.6
# <class 'float'>

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023221343873517788

print(rok // wiek)  # czesc całkowita dzielenia, 43, 2024/47 = 43.......
print(rok % wiek)  # modulo, reszta z dzielenia, 3
print(5 % 2)  # 1 bo 2 * 2 + 1r = 5

print(wiek ** rok)
# len() - zwraca długośc
print(len(str(wiek ** rok)))  # długośc 3385 znaków
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
# print(len(str(wiek ** rok ** 2)))  #

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# w przypadku liczb zmiennoprzecinkowych wystąpi bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# in a floating-point arithmetic with five base-ten digits of precision, the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# 1.3 x 10 ^ 3 -> 1.3 x 2 ^ 4
# decimal - typ do liczenia pieniędzy
print(sys.float_info)
# sys.float_info(
#     max=1.7976931348623157e+308,
#     max_exp=1024,
#     max_10_exp=308,
#     min=2.2250738585072014e-308,
#     min_exp=-1021,
#     min_10_exp=-307,
#     dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")  # Sprawdzenie zmiennej 36.6 47
print(f"""
{temp}
    {wiek}""")
# "36.6
#      47"

# typ logiczny
# prawda, fałsz
# True, False
# 1 - prawda, 0 - fałsz
czy_znasz_pythona = True
print(type(czy_znasz_pythona))  # <class 'bool'>, typ logiczny
print(czy_znasz_pythona)  # True

print(int(czy_znasz_pythona))  # 1, int - rzutowanie na liczbę integer
print(int(False))  # 0

print(bool(1))  # True, bool() - rzutowanie na typ logiczny
print(bool(100))  # True
print(bool(100))  # True
print(bool(-10))  # True
print(bool(-10))  # True
print(bool(-6.8))  # True
print(bool(-6.8))  # True
print(bool("radek"))  # True
print(bool(" "))  # True

print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False, None nic, stan nieokreslony

print("--------")
# działania logiczne
# and -> i
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# or - lub
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True
