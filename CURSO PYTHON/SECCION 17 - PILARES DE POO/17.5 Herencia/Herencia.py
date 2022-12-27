class Animales():
    def habla(self):
        print("Yo soy un animal")

    def descripcion(self):
        print("Yo soy una {}".format(self.animal))   

class Perro(Animales):
    pass #Es la forma de indicarle a Python que no vamos agregar nada.

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal



animal = Animales()
animal.habla()

perro = Perro()
perro.habla() 

abeja = Abeja("Abeja")
abeja.descripcion()
