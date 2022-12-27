import turtle

s = turtle.Screen()
t = turtle.Turtle() #turtle = Módulo; Turtle = Clase dentro de la librería

'''t.backward(100) #Desplaza la tortula 100 px hacia atrás
t.right(90) #Desplaza la tortula 90° hacia la derecha
t.forward(100) #Desplaza la tortula 100 px hacia adelante
t.left(90) #Desplaza la tortula 90° hacia la izquierda
t.forward(100)'''

#otra forma de escribir lo anterior. 
t.fd(100) 
t.rt(90)
t.fd(100)
t.lt(90)
t.bk(100)

turtle.done() #Permite abrir la pantalla y se mantenga abierta
