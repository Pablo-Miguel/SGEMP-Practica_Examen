"""
import math

def collision(rleft, rtop, width, height,   # rectangle definition
              center_x, center_y, radius):  # circle definition
    # Detect collision between a rectangle and circle.

    # complete boundbox of the rectangle
    rright, rbottom = rleft + width/2, rtop + height/2

    # bounding box of the circle
    cleft, ctop     = center_x-radius, center_y-radius
    cright, cbottom = center_x+radius, center_y+radius

    # trivial reject if bounding boxes do not intersect
    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False  # no collision possible

    # check whether any point of rectangle is inside circle's radius
    for x in (rleft, rleft+width):
        for y in (rtop, rtop+height):
            # compare distance between circle's center point and each point of
            # the rectangle with the circle's radius
            if math.hypot(x-center_x, y-center_y) <= radius:
                return True  # collision detected

    # check if center of circle is inside rectangle
    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True  # overlaid

    return False  # no collision detected
"""

import pygame
from os import *

#Inicilización de Pygame
pygame.init()

#Inicialización de la superficie de dibujo
WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

#Titulo del juego
pygame.display.set_caption("Simumlacro examen 2")

ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

FONT = pygame.font.Font(None, 40)

cont_nav1 = 0
cont_nav2 = 0

nave1 = pygame.Rect(150, 50, 30, 30)
speed_nave1 = [0, 0]

nave2 = pygame.Rect(450, 50, 30, 30)
speed_nave2 = [0, 0]

bala1 = pygame.Rect(-50, -50, 10, 10)
speed_bala1 = [0, 0]

bala2 = pygame.Rect(-50, -50, 10, 10)
speed_bala2 = [0, 0]

def disparar_nave1():
    bala1.x = nave1.x + nave1.width / 2 - bala1.width / 2
    bala1.y = nave1.y + nave1.height / 2 - bala1.height / 2
    speed_bala1[0] = 4

def disparar_nave2():
    bala2.x = nave2.x + nave2.width / 2 - bala2.width / 2
    bala2.y = nave2.y + nave2.height / 2 - bala2.height / 2
    speed_bala2[0] = -4

#Bucle principal del juego
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed_nave1[0] = -3
                speed_nave1[1] = 0
            if event.key == pygame.K_d:
                speed_nave1[0] = 3
                speed_nave1[1] = 0
            if event.key == pygame.K_w:
                speed_nave1[1] = -3
                speed_nave1[0] = 0
            if event.key == pygame.K_s:
                speed_nave1[1] = 3
                speed_nave1[0] = 0
            if event.key == pygame.K_LEFT:
                speed_nave2[0] = -3
                speed_nave2[1] = 0
            if event.key == pygame.K_RIGHT:
                speed_nave2[0] = 3
                speed_nave2[1] = 0
            if event.key == pygame.K_UP:
                speed_nave2[1] = -3
                speed_nave2[0] = 0
            if event.key == pygame.K_DOWN:
                speed_nave2[1] = 3
                speed_nave2[0] = 0
            if event.key == pygame.K_SPACE:
                disparar_nave1()
            if event.key == pygame.K_RSHIFT:
                disparar_nave2()

    if nave1.left < 0 or nave1.right > ventana.get_width() / 2:
        speed_nave1[0] = -speed_nave1[0]
    if nave1.top < 0 or nave1.bottom > ventana.get_height():
        speed_nave1[1] = -speed_nave1[1]

    if nave2.left < ventana.get_width() / 2 or nave2.right > ventana.get_width():
        speed_nave2[0] = -speed_nave2[0]
    if nave2.top < 0 or nave2.bottom > ventana.get_height():
        speed_nave2[1] = -speed_nave2[1]
    
    if bala1.left < 0 or bala1.right > ventana.get_width():
        speed_bala1[0] = 0
        bala1.x = -50
        bala1.y = -50
    if bala2.left < 0 or bala2.right > ventana.get_width():
        speed_bala2[0] = 0
        bala2.x = -50
        bala2.y = -50

    if bala1.colliderect(nave2):
        cont_nav1 += 1
        bala1.x = -50
        bala1.y = -50
    
    if bala2.colliderect(nave1):
        cont_nav2 += 1
        bala2.x = -50
        bala2.y = -50

    ventana.fill((252, 243, 207))

    pygame.draw.line(ventana, ROJO, (ventana.get_width() / 2, 0), (ventana.get_width() / 2, ventana.get_height()))

    nave1 = nave1.move(speed_nave1)
    nave2 = nave2.move(speed_nave2)
    bala1 = bala1.move(speed_bala1)
    bala2 = bala2.move(speed_bala2)

    pygame.draw.rect(ventana, ROJO, nave1, 0)
    pygame.draw.rect(ventana, ROJO, nave2, 0)
    pygame.draw.rect(ventana, NEGRO, bala1, 0)
    pygame.draw.rect(ventana, NEGRO, bala2, 0)

    scores = FONT.render(f'{cont_nav1}          {cont_nav2}', True, NEGRO)
    ventana.blit(scores, (ventana.get_width() / 2 - scores.get_width() / 2, 20))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()