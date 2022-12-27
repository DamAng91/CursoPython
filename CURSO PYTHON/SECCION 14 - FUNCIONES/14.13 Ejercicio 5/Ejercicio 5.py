import math

def cuadrado(base,altura):
    area = base * altura
    return ("El area del cuadrado es:", area)

print(cuadrado(20, 20))


def circulo(radio):
    area = pow(radio,2)*3.14
    return ("El area del circulo es:", area)

print(circulo(10))