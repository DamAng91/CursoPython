diccionario = {
    "Guatemala": "Ciudad de Guatemala", 
    "El Salvador": "San Salvador", 
    "Honduras": "Tegucigalpa", 
    "Nicaragua": "Managua", 
    "Costa Rica": "San Jose", 
    "Panama": "Panama", 
    "Argentina": "Buenos Aires", 
    "Colombia": "Bogota", 
    "Venezuela": "Caracas", 
    "Espania": "Madrid"
    }

pais = input("Ingrese el nombre de un pais: ")
'''letra = pais.capitalize() in diccionario

if letra == True: #otra nomenclatura es if letra: 
    print(diccionario[pais.capitalize()])
else:
    print("El pais no se encuentra en el diccionario")'''

if pais.capitalize() in diccionario:
    print(diccionario[pais.capitalize()])
else:
    print("El pais no se encuentra en el diccionario")


#Nótese que Costa Rica arroja eror, esto es dado el espacio.
#Averiguar por que ocurre