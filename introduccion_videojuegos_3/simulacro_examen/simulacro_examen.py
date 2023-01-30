"""
BATALLA DE NAVES
- Dos naves
- Dos campos
- Cada nave se controla con keys diferentes
- Cada jugador dispara con una tecla
"""

import random
import time
import turtle

# Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego del Pong")
wn.bgcolor("black")
wn.setup(width=600, height=600)
# Para que se vea mejor
wn.tracer(0)

line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.penup()
line.goto(0, 0)
line.shapesize(150, 0.02, 1)
line.direction = "stop"

# Nave 1
nave1 = turtle.Turtle()
nave1.speed(0)
nave1.shape("square")
nave1.color("white")
nave1.penup()
nave1.goto(-150, 0)
nave1.direction = "stop"

# Nave 2
nave2 = turtle.Turtle()
nave2.speed(0)
nave2.shape("square")
nave2.color("white")
nave2.penup()
nave2.goto(150, 0)
nave2.direction = "stop"

#Bala nave 1
balaNave1 = turtle.Turtle()
balaNave1.speed(0)
balaNave1.shape("circle")
balaNave1.color("red")
balaNave1.penup()
balaNave1.goto(1000, 1000)
balaNave1.direction = "stop"

#Bala nave 2
balaNave2 = turtle.Turtle()
balaNave2.speed(0)
balaNave2.shape("circle")
balaNave2.color("green")
balaNave2.penup()
balaNave2.goto(1000, 1000)
balaNave2.direction = "stop"

def dispararNave1():
    balaNave1.goto(nave1.xcor(), nave1.ycor())
    balaNave1.direction = "right"

def dispararNave2():
    balaNave2.goto(nave2.xcor(), nave2.ycor())
    balaNave2.direction = "left"

def arribaNave1():
    nave1.direction = "up"
def abajoNave1():
    nave1.direction = "down"
def arribaNave2():
    nave2.direction = "up"
def abajoNave2():
    nave2.direction = "down"

SPEED_NAVE1 = 20
def movNave1():
    if nave1.direction == "up":
        y = nave1.ycor()
        nave1.sety(y + SPEED_NAVE1)
    elif nave1.direction == "down":
        y = nave1.ycor()
        nave1.sety(y - SPEED_NAVE1)

SPEED_NAVE2 = 20
def movNave2():
    if nave2.direction == "up":
        y = nave2.ycor()
        nave2.sety(y + SPEED_NAVE2)
    elif nave2.direction == "down":
        y = nave2.ycor()
        nave2.sety(y - SPEED_NAVE2)

SPEED_BALA_NAVE1 = 20
def movBalaNave1():
    if balaNave1.direction == "right":
        x = balaNave1.xcor()
        balaNave1.setx(x + SPEED_BALA_NAVE1)

SPEED_BALA_NAVE2 = 20
def movBalaNave2():
    if balaNave2.direction == "left":
        x = balaNave2.xcor()
        balaNave2.setx(x - SPEED_BALA_NAVE2)

wn.listen()
wn.onkeypress(arribaNave1, "w")
wn.onkeypress(abajoNave1, "s")
wn.onkeypress(dispararNave1, "d")
wn.onkeypress(arribaNave2, "Up")
wn.onkeypress(abajoNave2, "Down")
wn.onkeypress(dispararNave2, "Left")

score_nav1 = 0
score_nav2 = 0

text = turtle.Turtle()
text.speed(0)
text.shape("square")
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 250)
text.write(f"{score_nav1}          {score_nav2}", align="center", font=("candra", 24, "bold"))

POSPONER = 0.1

while True:
    wn.update()

    # Colisiones bordes
    if nave1.xcor() > 280 or nave1.xcor() < -280 or nave1.ycor() > 280 or nave1.ycor() < -280:
        nave1.direction = "stop"
    if nave2.xcor() > 280 or nave2.xcor() < -280 or nave2.ycor() > 280 or nave2.ycor() < -280:
        nave2.direction = "stop"
    if balaNave1.xcor() > 280 or balaNave1.xcor() < -280 or balaNave1.ycor() > 280 or balaNave1.ycor() < -280:
        balaNave1.direction = "stop"
        balaNave1.goto(1000, 1000)
    if balaNave2.xcor() > 280 or balaNave2.xcor() < -280 or balaNave2.ycor() > 280 or balaNave2.ycor() < -280:
        balaNave2.direction = "stop"
        balaNave2.goto(1000, 1000)

    if balaNave1.distance(nave2) < 20:
        score_nav1 += 10
        text.clear()
        text.write(f"{score_nav1}          {score_nav2}", align="center", font=("candra", 24, "bold"))

    if balaNave2.distance(nave1) < 20:
        score_nav2 += 10
        text.clear()
        text.write(f"{score_nav1}          {score_nav2}", align="center", font=("candra", 24, "bold"))

    movNave1()
    movNave2()
    movBalaNave1()
    movBalaNave2()

    time.sleep(POSPONER)