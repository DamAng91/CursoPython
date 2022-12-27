import imp
import turtle
import random #Dado que vamos a "tirar un dado"


s = turtle.Screen()
s.title("Primero Proyecto")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

jugador1.shape("turtle")
jugador1.color("green", "green")

jugador2.shape("turtle")
jugador2.color("blue", "blue")

jugador1.penup()
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-250,225)

jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-250,-170)


turtle.done()