'''def factorial():
    num = int(input("Ingrese un numero entero positivo: "))
    if num >0:
        factorial = 1
        for i in range(1, num+1):
            factorial = factorial * i
        print(factorial)
    else:
        print("El numero es negativo y no podemos proceder")

factorial()'''

def factorial():
    from math import factorial
    num = int(input("Ingrese un numero entero positivo: "))
    if num >0:
        print(factorial(num))
    else:
        print("El numero es negativo y no podemos proceder")

factorial()