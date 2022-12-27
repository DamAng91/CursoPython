from typing import KeysView, ValuesView


diccionario = {
    1: "Casillas",
    15: "Ramos",
    3: "Pique",
    5: "Puyol",
    11: "Capdevilla",
    14: "Xabi Alonso",
    16: "Busquets",
    8: "Xabi Hernandez",
    18: "Pedrito",
    6: "Iniesta",
    7: "Villa"
}

clave = int(input("Ingrese un numero: "))

if clave in diccionario:
    print("El numero {} corresponde a: {}".format(clave, diccionario[clave]))
else:
    print("El numero {} no se encuentra en el diccionario".format(clave))