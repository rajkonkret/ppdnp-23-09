# funkcja wewnętrzna, zagnieżdzona
# uzywana w dekoratorach

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    # print(fun2) # <function fun1.<locals>.fun2 at 0x000001D0FF809EE0>
    return fun2  # zwracamy adres tej funkcji, referencje


fun1()  # To jest fun1
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x000001F7E86B9EE0>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
print(fun1())  # <function fun1.<locals>.fun2 at 0x0000021160907BA0>
fun1()()  # To jest fun2
