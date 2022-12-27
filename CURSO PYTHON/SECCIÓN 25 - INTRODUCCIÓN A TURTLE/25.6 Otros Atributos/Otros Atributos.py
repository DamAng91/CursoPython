import turtle

s = turtle.Screen()
t = turtle.Turtle()

'''t.begin_fill()
t.circle(100)
t.end_fill()

t.begin_fill()
t.color("white", "white")
t.circle(50)
t.end_fill()'''

t.shape("turtle") #Permite dar forma de tortuga al lapiz

t.fd(100)
t.penup() #Levanta la tortuga para que no trace 
t.fd(50)
t.pendown() #Baja la tortuga para que comience a trazar nuevamente
t.fd(100)

t.undo() #Retrocede la última acción de la tortuga
t.clear() #Limpia todo el trazo realizado por la tortuga
t.reset() #Resetea todo lo efectuado por la tortuga 

t.fd(100)
t.stamp() #Deja un sello de los movimientos efectuados
t.fd(100) 

turtle.done()