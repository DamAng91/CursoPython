nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

#print(nombre, edad) #La "," es un método de concatenación igual que el "+". 
#print("Hola", nombre, "tienes", edad)

print("Hola {} tienes {}".format(nombre,edad))