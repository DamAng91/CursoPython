import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10) #Permite darle velocidad al desplazamiento de la tortuga
t.circle(10) #La tortuga efectúa un círculo de radio 10px
t.speed(10)
t.circle(50)
t.dot(30) #La tortuga efectúa un punto de diámetro 30px

t.hideturtle() #Permite ocultar a la tortuga
t.speed(1)
t.circle(40)
t.showturtle() #Permite mostrar a la tortuga
t.circle(100)

t.setx(100) #Permite mantener el eje Y y modificar en 100px al X
t.sety(-100) #Permite mantener el eje x y modificar en 100px al Y

turtle.done()