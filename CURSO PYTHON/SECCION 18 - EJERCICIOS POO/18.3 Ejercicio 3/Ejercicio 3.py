'''class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    
class Moto(Fabrica):
    def Llantas(self):
        print("Llantas: {}".format(self.llantas))
    def Color(self):
        print("Color: {} ".format(self.color))
    def Precio(self):
        print("Precio: {} ".format(self.precio))

class Carro(Fabrica):
    def Llantas(self):
        print("Llantas: {}".format(self.llantas))
    def Color(self):
        print("Color: {} ".format(self.color))
    def Precio(self):
        print("Precio: {} ".format(self.precio))



moto = Moto(2, "Negra", 22000)
print("La moto tiene las siguientes caracteristicas: ")
moto.Llantas()
moto.Color()
moto.Precio()

carro = Carro(4, "Gris", 3000000)
print("El carro tiene las siguientes caracteristicas: ")
carro.Llantas()
carro.Color()
carro.Precio()'''

#Ejemplo
class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    
class Moto(Fabrica):
    def Datos(self):
        print("Llantas: {}".format(self.llantas))
        print("Color: {} ".format(self.color))
        print("Precio: $ {} ".format(self.precio))

class Carro(Fabrica):
    def Datos(self):
        print("Llantas: {}".format(self.llantas))
        print("Color: {} ".format(self.color))
        print("Precio: $ {} ".format(self.precio))


moto = Moto(2, "Negra", 4000)
moto.Datos()

carro = Carro(4, "Blanco", 5000)
carro.Datos()