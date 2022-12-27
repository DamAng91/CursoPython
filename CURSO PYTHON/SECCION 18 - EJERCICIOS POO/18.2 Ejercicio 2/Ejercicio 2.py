'''class Calculadora():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sumar(self):
        self.suma = self.x + self.y
        print("La suma es igual a: ", self.suma)

    def restar(self):
        self.resta = self.x - self.y
        print("La resta es igual a: ", self.resta)

    def multiplicar(self):
        self.mult = self.x * self.y
        print("La multiplicacion es igual a: ", self.mult)

    def dividir(self):
        self.division = self.x / self.y
        print("La division es igual a: ", self.division)


v1 = int(input("Ingrese el primer valor: "))
v2 = int(input("Ingrese el segundo valor: "))

calcular = Calculadora(v1, v2)
print(calcular.sumar())
print(calcular.restar())
print(calcular.multiplicar())
print(calcular.dividir())'''


#Ejemplo

class Calculadora():
    def __init__(self):
        self.x = int(input("Ingrese el primer valor: "))
        self.y = int(input("Ingrese el segundo valor: "))

    def sumar(self):
        self.suma = self.x + self.y
        print("La suma es igual a: ", self.suma)

    def restar(self):
        self.resta = self.x - self.y
        print("La resta es igual a: ", self.resta)

    def multiplicar(self):
        self.mult = self.x * self.y
        print("La multiplicacion es igual a: ", self.mult)

    def dividir(self):
        self.division = self.x / self.y
        print("La division es igual a: ", self.division)

calcular = Calculadora()
print(calcular.sumar())
print(calcular.restar())
print(calcular.multiplicar())
print(calcular.dividir())