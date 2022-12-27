tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

numero = int(input("Ingrese el numero del mes: "))

print("El numero {} corresponde al mes: {}".format(numero, tupla[numero-1]))
