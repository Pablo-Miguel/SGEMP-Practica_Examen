import pygame
from os import *

pygame.init()

WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Ejemplo 2")

#Creamos el objeto pelota
ball = pygame.image.load(getcwd() + "\\introduccion_videojuegos\\ejemplo2\\assets\\imgs\\ball.png")
ball = pygame.transform.scale(ball, (40, 40))

#Obtengo el rectángulo del objeto anterior
ballrect = ball.get_rect()

#Introduzco los valores con los que se van a mover la pelota. El primer valor representa
speed = [4,4]

#Pongo la pelota en el origen de coordenadas
ballrect.move_ip(0,0)

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Muevo la pelota
    ballrect = ballrect.move(speed)

    #Comprobamos si la pelota ha llegado a los límites de la ventana
    #Eje -> X
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    #Eje -> Y
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    ventana.fill((255, 105, 180))
    #Dibujo la pelota
    ventana.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()