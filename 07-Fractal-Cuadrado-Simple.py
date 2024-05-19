import turtle
ventana = turtle.Screen()
ventana.bgcolor("black")
tortuga = turtle.Turtle()
turtle.speed(0)
tortuga.color('red')
Longitud = 10
Aumento = 1/2*Longitud
angulo = 90
vueltas = 100000
for _ in range(vueltas):
    for _ in range(4):
        tortuga.forward(Longitud)
        tortuga.right(90)
    tortuga.right(180)
    tortuga.forward(Aumento/4)
    tortuga.right(90)
    tortuga.forward(Aumento/4)
    tortuga.right(90)
    Longitud = Longitud + 2*Aumento

ventana.exitonclick()


