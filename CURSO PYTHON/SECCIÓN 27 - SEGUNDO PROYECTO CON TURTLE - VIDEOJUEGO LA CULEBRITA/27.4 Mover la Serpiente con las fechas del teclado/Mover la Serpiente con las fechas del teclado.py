import turtle
import time

retraso = 0.1

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

def arriba():
    serpiente.direction = 'up'

def abajo():
    serpiente.direction = 'down'

def derecha():
    serpiente.direction = 'right'

def izquierda():
    serpiente.direction = 'left'

def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor() #Creo una variable que permite direccionar la serpiente al eje Y
        serpiente.sety(y + 20) #Permite el movimiento de la serpiente por desplazamiento de 20px sobre el eje Y positivo
    if serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x - 20)

s.listen() #Permite que la pantalla "escuche" las teclas que presiono
s.onkeypress(arriba, "Up") #Escucha la tecla que presiono, en este caso, Tecla flecha hacia arriba activa la función Arriba
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")

while True:
    s.update() #Actualiza la pantalla constantemente 
    movimiento()
    time.sleep(retraso)




turtle.done()