conjunto = {1, 2, 3, 4, 5}
#lista = [1, 1, 2, 3, 4, 4]

#print(lista)
print(conjunto) #Nótese que no se imprimen los datos repetidos en el conjunto

conjunto.add(20) #Añade un nuevo dato, en este caso, el 20
print(conjunto)

conjunto.remove(1) #Elimina el elemento del conjunto, en este caso, el 1
print(conjunto)

conjunto.pop() #Elimina el primer elemento del conjunto: "2"
print(conjunto)

conjunto.update([1, 2, 3]) #Añade elementos iterables pero NO repetidos
print(conjunto)

conjunto.clear()
print(conjunto)
