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
# Elegimos la cantidad lados que tendrá el polígono
L = 3
# Elegimos la longitud de cada lado del polígono
Longitud = 2
# Hacemos el angulo de forma que dependa de L
angulo = 180 - ((L - 2)*180/L) 
# Hacemos la iteración total de C veces
C = 30
# Esta será la desviación al final de cada dibujo
Desviación = 111
EscapeDelDibujo = 10*Longitud
#Este loop dará vueltas todo:
for _ in range(C):
    #

# Este es el loop que dará vida al programa
    for _ in range(C):
         #
   
# iteración del primer polígono
         for _ in range(L):
             #
            tortuga.right(angulo)
            tortuga.forward(Longitud)
    # El polígono vuelve al punto de partida

         tortuga.right(180)
         tortuga.forward(Longitud)
         tortuga.right(Desviación)
   
   # El polígono hace lo mismo de nuevo
         for _ in range(L):

           tortuga.right(angulo)
           tortuga.forward(Longitud)
    # el polígono es reposicionado

    tortuga.right(180)
    tortuga.forward(Longitud)
    tortuga.right(Desviación)
    tortuga.forward(EscapeDelDibujo)

    for _ in range(C):
   
# iteración del primer polígono
        for _ in range(L):
           tortuga.right(angulo)
           tortuga.forward(Longitud)
    # El polígono vuelve al punto de partida

        tortuga.right(180)
        tortuga.forward(Longitud)
        tortuga.right(Desviación)
   
   # El polígono hace lo mismo de nuevo
        for _ in range(L):

           tortuga.right(angulo)
           tortuga.forward(Longitud)
    # el polígono es reposicionado

    tortuga.right(180)
    tortuga.forward(Longitud)
    tortuga.right(Desviación)
    tortuga.forward(EscapeDelDibujo)

# Ejecutamos el programa
ventana.exitonclick()
