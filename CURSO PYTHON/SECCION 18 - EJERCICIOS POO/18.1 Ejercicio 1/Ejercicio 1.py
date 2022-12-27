'''Resuelto por mi

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def resultado(self):
        if self.nota >= 7:
            return "El alumno ha aprobado"
        else:
            return "El alumno ha desaprobado"



alumno = Estudiante("Pedro", 7)
print(alumno.nombre)
print(alumno.nota) 
print(alumno.resultado())'''


#Ejemplo 1:

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre, self.nota))

    def resultado(self):
        if self.nota < 7:
            print("Has REPROBADO!")
        else:
            print("Has APROBADO!")



estudiante1 = Estudiante("Daniel", 10)
estudiante1.imprimir()
estudiante1.resultado()


estudiante2 = Estudiante("Karla", 5)
estudiante2.imprimir()
estudiante2.resultado()

'''#Ejemplo 2:

class Estudiante():
    def datos(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre, self.nota))

    def resultado(self):
        if self.nota < 7:
            print("Has REPROBADO!")
        else:
            print("Has APROBADO!")



estudiante1 = Estudiante()
estudiante1.datos("Daniel", 10)
estudiante1.imprimir()
estudiante1.resultado()
'''