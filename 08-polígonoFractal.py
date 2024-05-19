import turtle
ventana = turtle.Screen()
ventana.bgcolor("black")
tortuga = turtle.Turtle()
turtle.speed(1)
tortuga.color('red')
L = 3.14
Longitud = 20
Aumento = 1/2*Longitud
angulo = 180 - ((L - 2)*180/L) 
vueltas = 100
for _ in range(vueltas):
    for _ in range(4):
        tortuga.forward(Longitud)
        tortuga.right(angulo)
    tortuga.right(180)
    tortuga.forward(Aumento)
    tortuga.right(90)
    tortuga.forward(Aumento)
    tortuga.right(90)
    Longitud = Longitud + 2*Aumento

ventana.exitonclick()