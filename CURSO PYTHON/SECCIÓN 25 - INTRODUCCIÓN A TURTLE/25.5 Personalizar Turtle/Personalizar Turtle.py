import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("red") #Permite cambiar de color el fondo de la pantalla
s.title("Proyecto 1") #Permite cambiar el nombre del lienzo

t.shapesize(3,3,3) #Permite modificar el ancho, largo y borde de la tortuga respectivamente
t.fillcolor("orange") #Permite cambiar el color de la tortuga
t.fd(100)

t.pencolor("white") #Permite cambiar el color del borde de la tortuga y su desplazamiento
t.fd(100)

t.color("green", "blue") #Otra manera de cambiar el borde y trazo y color de la tortuga
t.rt(90)
t.fd(100)

t.pensize(5) #Permite cambiar el grosor del desplazamiento de la tortuga
t.fd(100)


turtle.done()