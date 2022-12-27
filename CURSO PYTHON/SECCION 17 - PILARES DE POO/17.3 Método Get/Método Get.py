class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0


    @property #Implica que, el siguiente método, va a ser considerado como un método Get, es decir, como un atributo
    def cuenta(self):
        return self._cuenta

    @property
    def contador(self):
        return self._contador


a = A()
print(a.cuenta) #Es una buena practica llamar al método por atributo cuando se utilza el Property
#print(a.cuenta()) Es una buena practica llamar por método cuando no se utilza el Propety
print(a.contador)



