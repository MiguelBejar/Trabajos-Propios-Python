# importamos la libreria turtle
import turtle
# hacemos que la ventana se active
ventana = turtle.Screen()
# elegimos el color de fondo
ventana.bgcolor("black")
# Activamos la tortuga
tortuga = turtle.Turtle()
# Elegimos la velocidad de coloreo
tortuga.speed(0)
# el color de la tortuga
tortuga.color('red')
# Elegimos la longitud de cada lado del triangulo
longitud = 150
angulo = 144
# Hacemos la iteración de 5 veces
for _ in range(10):
    
    for _ in range(5):
        tortuga.forward(longitud)
        # Este es el giro de 144 grados
        tortuga.right(angulo)
    tortuga.right(300)
    tortuga.forward(longitud/10)
    tortuga.right(65)
    #tortuga.forward(longitud/10)
    for _ in range(5):
       tortuga.forward(longitud)
       # Este es el giro de 144 grados
       tortuga.right(angulo)


ventana.exitonclick()
