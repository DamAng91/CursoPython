numero = int(input("Ingrese un numero: "))

'''if numero >=0: 
    print("El valor absoluto es: ", numero)
else:
    print("El valor absoluto es: ", -1*numero)'''

if numero >0:
    print("El valor absoluto de {} es: {}".format(numero,numero))
else:
    print("El valor absoluto de {} es: {}".format(numero,abs(numero)))
