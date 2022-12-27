diccionario = {'Nombre': "Damian", 'Apellido': "Angelucci", 'Estatura': 1.78}

print(diccionario)
print(diccionario.keys()) #Devuelve sólo las claves y NO el valor.
print(diccionario.values()) #Devuelvo sólo los valores y NO las claves.

print(diccionario['Estatura']) #Devuelve sólo el valor de la clave "Estatura"

diccionario["Peso"] = "58 kg" #Permite agregar una clave y su valor
print(diccionario) 

diccionario['Nombre'] = "Walter"
print(diccionario)