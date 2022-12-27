def funcion():
    num = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    if num > num2:
        return 1
    elif num2 > num:
        return -1
    else:
        return 0

print(funcion)