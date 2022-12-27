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

jugador1.goto(0,200)


turtle.done()