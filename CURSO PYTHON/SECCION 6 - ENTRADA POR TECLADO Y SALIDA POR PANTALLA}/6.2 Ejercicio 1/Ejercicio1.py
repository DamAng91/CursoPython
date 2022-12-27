#a = float(input("Ingrese el valor de a:"))
#b = float(input("Ingrese el valor de b:"))
#c = float(input("Ingrese el valor de c:"))

#dividendo = (-b+pow(((pow(b,2))-4*a*c),1/2))
#divisor = 2*a
#x = dividendo/divisor

#print("La solucion es:", x)

#Ejemplo
#3x^2-5x-2 =0  x=1 x=2/3

from math import sqrt

a = int(input("Ingrese el valor de a:"))
b = int(input("Ingrese el valor de b:"))
c = int(input("Ingrese el valor de c:"))

x1 = 0
x2 = 0

if ((b**2)-4*a*c) < 0:
    print("No se puede realizar dado que la raiz es negativa")
else:
    x1 = (-b+ (sqrt((b**2)-4*a*c)))/(2*a)
    x2 = (-b- (sqrt((b**2)-4*a*c)))/(2*a)

print("La solucion es: \n", x1, "\nx2:", x2)



