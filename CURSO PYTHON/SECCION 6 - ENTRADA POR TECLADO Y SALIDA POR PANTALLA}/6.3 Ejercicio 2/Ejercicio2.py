#P1 = float(input("Ingrese la nota de la Practica 1:"))
#P2 = float(input("Ingrese la nota de la Practica 2:"))
#P3 = float(input("Ingrese la nota de la Practica 3:"))

#PP = (P1+P2+P3)/3

#print("El promedio de las practicas es:", PP)

#EP = float(input("Ingrese la nota del Examen Parcial:"))
#EF = float(input("Ingrese la nota del Examen Final:"))

#PROM = (PP+2*EP+3*EF)/6

#print("El promedio total resulta:", PROM)


practica1 = float(input("Ingrese el valor de la practica 1: "))
practica2 = float(input("Ingrese el valor de la practica 2: "))
practica3 = float(input("Ingrese el valor de la practica 3: "))
ExamanParcial = float(input("Ingrese el valor del examen parcial: "))
ExamanFinal = float(input("Ingrese el valor del examen final: "))

PromedioPractica = (practica1 + practica2 + practica3)/3

PromedioFinal = (PromedioPractica + 2*ExamanParcial+ 3*ExamanFinal) /6

print("El promedio final del estudiante es de:\n", PromedioPractica, "\nY el promedio final es de:", PromedioFinal)