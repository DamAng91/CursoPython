import turtle

s = turtle.Screen()
s.setup(650, 650) #Define el tamaño de la pantalla
s.bgcolor("gray")
s.title("Proyecto 2")

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop' 
serpiente.color("green")

turtle.done()