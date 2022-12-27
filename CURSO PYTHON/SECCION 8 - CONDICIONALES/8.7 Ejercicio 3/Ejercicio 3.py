palabra1 = input("Ingrese la primer palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

'''if palabra1[-3: ] == palabra2[-3: ]:
    print("{} y {} riman". format(palabra1,palabra2))
elif palabra1[-2: ] == palabra2[-2: ]:
    print("{} y {} riman un poco". format(palabra1,palabra2))
else:
    print("{} y {} NO riman". format(palabra1,palabra2))'''

if len(palabra1) < 3 or len(palabra2) < 3:
    print("NO rima, porque tienen menos de 3 caracteres")
elif palabra1[-3: ] == palabra2[-3: ]:
    print("Las palabras riman") 
elif palabra1[-2: ] == palabra2[-2: ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")
   