import random
import time
import turtle

# Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego del Pong")
wn.bgcolor("hotpink")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("black")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Segmentos / cuerpo serpiente
segmentos = []

#Texto
score = 0
high_score = 0

text = turtle.Turtle()
text.speed(0)
text.shape("square")
text.color("black")
text.penup()
text.hideturtle()
text.goto(0, 250)
text.write(f"Score: {score}  High Score: {high_score}", align="center", font=("candra", 24, "bold"))

# Funciones
def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def izquierda():
    cabeza.direction = "left"


def derecha():
    cabeza.direction = "right"


SPEED = 20
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + SPEED)
    elif cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - SPEED)
    elif cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - SPEED)
    elif cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + SPEED)


# Teclado
wn.listen()
wn.onkeypress(arriba, "w")
wn.onkeypress(abajo, "s")
wn.onkeypress(izquierda, "a")
wn.onkeypress(derecha, "d")
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

POSPONER = 0.1

while True:
    wn.update()

    # Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        for element in segmentos:
            element.goto(1000, 1000)

        segmentos.clear()

        score = 0
        text.clear()
        text.write(f"Score: {score}  High Score: {high_score}", align="center", font=("candra", 24, "bold"))

        time.sleep(1)

    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        score += 10

        if high_score < score:
            high_score = score

        text.clear()
        text.write(f"Score: {score}  High Score: {high_score}", align="center", font=("candra", 24, "bold"))


    # Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()

    # Colisiones cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            for element in segmentos:
                element.goto(1000, 1000)

            segmentos.clear()

            score = 0
            text.clear()
            text.write(f"Score: {score}  High Score: {high_score}", align="center", font=("candra", 24, "bold"))

            time.sleep(1)

    time.sleep(POSPONER)
