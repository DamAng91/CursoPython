class Universidad ():
    def __init__(self, nombreU):
        self.nombreU = nombreU

class Carrera():
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, nombreU, especialidad, nombre, edad):
        super().__init__(nombreU)
        super().__init__(especialidad)
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Universidad: ", self.nombreU)
        print("Carrera: ", self.especialidad)

persona = Estudiante("UTN", "Ing. Naval", "Damian", 30)
persona.datos()


'''#Ejemplo
class Universidad ():
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es {}, tengo {} anios, mi especialidad {} en {}".format(self.nombre, self.edad, self.especialidad, self.Nombre))


persona = Estudiante("Don Bosco")
persona.carrera("Sistemas")
persona.datos("Carlos", 20)
'''
