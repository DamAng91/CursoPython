class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0

    def incrementar(self):
        self._contador +=1

    def cuenta (self):
        return self._contador

a = A()
'''print(a._cuenta) 
a._cuenta = 20
print(a._cuenta) 

Cuando se utiliza un atributo encapsulado, estas maneras son MALAS PRÁCTICAS
para cambiar el valor de un atributo y/o imprimirlo.
''' 
