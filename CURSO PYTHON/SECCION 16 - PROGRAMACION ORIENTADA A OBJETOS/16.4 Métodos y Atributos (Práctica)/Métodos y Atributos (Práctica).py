class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRAM = 32
    almacenamiento = 128
#Huawi, Negro, 32, 128 son atributos

    def llamar(self, mensaje): #Es una funcion dentro de una clase: Metodo (de instancia)
            return mensaje

    def escucharMusica(self): #Los métodos de instancia llevan self en su argumento 
        print("Estas escuchando Musica")

telefono = FabricaTelefonos() #telefono es un objeto
print(telefono.marca) 
print(telefono.color)
print(telefono.memoriaRAM)
print(telefono.almacenamiento) #Forma de asignar un atributo a un objeto

print(telefono.llamar("Hola, Con quien hablo?"))
telefono.escucharMusica()