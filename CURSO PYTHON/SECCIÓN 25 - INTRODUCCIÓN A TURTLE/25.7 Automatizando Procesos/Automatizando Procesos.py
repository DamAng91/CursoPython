import turtle

s = turtle.Screen()
t = turtle.Turtle()

'''t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)'''

'''for i in range(4):
    t.fd(100)
    t.rt(90)'''

'''t.circle(100)
t.circle(90)
t.circle(80)
t.circle(70)
t.circle(60)
t.circle(50)
t.circle(40)
t.circle(30)
t.circle(20)
t.circle(10)'''

i = 0
resultado = input ("Quieres imprimir una figura?")
if resultado == "si":
    while i <= 100:
        t.circle(i)
        i +=10

else:
    print("Oka")

turtle.done()