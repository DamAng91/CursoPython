letra = input("Ingrese una letra: ")

'''if letra.lower() == "a":
    print("La letra ingresada es la vocal A")
elif letra.lower() == "e":
    print("La letra ingresada es la vocal E")
elif letra.lower() == "i":
   print("La letra ingresada es la vocal I")
elif letra.lower() == "o":
    print("La letra ingresada es la vocal O")
elif letra.lower() == "u":
    print("La letra ingresada es la vocal")

else:
    print("La letra ingresada NO es una vocal")'''

if letra.lower() in "aeiou":
    print("La letra ingresada es una vocal")
else:
    print("La letra ingresada NO es una vocal")

