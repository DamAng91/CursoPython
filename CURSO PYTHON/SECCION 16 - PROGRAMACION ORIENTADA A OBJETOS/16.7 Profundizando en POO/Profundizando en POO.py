class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Alcatel", "Negro", "Azul", "Rojo", m1 = 500, m2 = 1000)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512 #Es un atributo TEMPORAL 
print(telefono.memoria)