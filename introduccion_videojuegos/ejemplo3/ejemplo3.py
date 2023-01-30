import pygame
from os import *

pygame.init()

WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Ejemplo 3")

bg = pygame.image.load("introduccion_videojuegos/ejemplo3/assets/imgs/bg.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

#Creo el objeto pelota
ball = pygame.image.load("introduccion_videojuegos/ejemplo3/assets/imgs/ball.png")
ball = pygame.transform.scale(ball, (40, 40))
ballrect = ball.get_rect()
speed = [4,4]
ballrect.move_ip(0,0)

#Crea el objeto bate, y obtengo el rectángulo
bate = pygame.image.load("introduccion_videojuegos/ejemplo3/assets/imgs/bate.png")
bate = pygame.transform.scale(bate, (100, 49))
baterect = bate.get_rect()

#Pongo el bate en la parte inferior de la pantalla
baterect.move_ip((WIDTH / 2) - bate.get_width() , HEIGHT - bate.get_height())

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        baterect = baterect.move(-3, 0)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        baterect = baterect.move(3, 0)

    #Compruebo si hay colision
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    ventana.fill((255, 105, 180))
    ventana.blit(bg, (0,0))
    ventana.blit(ball, ballrect)
    ventana.blit(bate, baterect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()