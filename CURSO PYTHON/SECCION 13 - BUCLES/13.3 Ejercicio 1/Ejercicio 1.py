'''n = int(input("Ingrese un numero: "))

i = 0
while i <= 10:
    print("Tabla de multiplicacion: {} x {} = {}".format(n, i, n*i))
    i +=1'''

numero = int(input("Ingresa un numero: "))

i = 0
multi = 0

while i <= 10:
    multi = numero * i
    print("{} x {} = {}".format(numero, i, multi))
    i +=1