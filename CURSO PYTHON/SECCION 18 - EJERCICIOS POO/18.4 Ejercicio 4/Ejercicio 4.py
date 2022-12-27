'''class Marino():
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def hablar(self):
        print(self.mensaje)

class Pulpo(Marino):
    def hablar(self):
        print("Soy un Pulpo")

class Foca(Marino):
    def hablar(self):
        print(self.mensaje)

marino = Marino("Hola...")
marino.hablar()

pulpo = Pulpo("Hola...")
pulpo.hablar()

foca = Foca("Yo soy una Foca")
foca.hablar()'''

#Ejemplo:
class Marino():
    def hablar(self):
        print("Hola...")

class Pulpo(Marino):
    def hablar(self):
        print("Soy un Pulpo")

class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(self.mensaje)

marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola, soy una Foca")
