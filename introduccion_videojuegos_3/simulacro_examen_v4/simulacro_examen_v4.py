import pygame
from os import *
from random import *

#Inicilización de Pygame
pygame.init()

FONT = pygame.font.Font(None, 40)
cont_bate1 = 0
cont_bate2 = 0

#Inicialización de la superficie de dibujo
WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

#Titulo del juego
pygame.display.set_caption("Simumlacro examen 4")

ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

FONT = pygame.font.Font(None, 40)

ball = pygame.image.load("introduccion_videojuegos/ejemplo4/assets/imgs/ball.png")
ball = pygame.transform.scale(ball, (40, 40))
ballrect = ball.get_rect()
speed = [randint(3, 6), randint(3, 6)]
ballrect.move_ip(WIDTH / 2, HEIGHT / 2)

bate1 = pygame.Rect(0, HEIGHT / 2 - 150 / 2, 20, 150)

bate2 = pygame.Rect(WIDTH - 20, HEIGHT / 2 - 150 / 2, 20, 150)

#Bucle principal del juego
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ballrect = ballrect.move(speed)

    if ballrect.left < 0:
        speed[0] = -speed[0]
        cont_bate2 += 1
    elif ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
        cont_bate1 += 1

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    if bate1.colliderect(ballrect):
        speed[0] = -speed[0]
    
    if bate2.colliderect(ballrect):
        speed[0] = -speed[0]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bate1 = bate1.move(0, -5)
    if keys[pygame.K_s]:
        bate1 = bate1.move(0, 5)
    if keys[pygame.K_UP]:
        bate2 = bate2.move(0, -5)
    if keys[pygame.K_DOWN]:
        bate2 = bate2.move(0, 5)

    if bate1.top < 0:
        bate1 = bate1.move(0, 5)
    elif bate1.bottom > ventana.get_height():
        bate1 = bate1.move(0, -5)
    
    if bate2.top < 0:
        bate2 = bate2.move(0, 5)
    elif bate2.bottom > ventana.get_height():
        bate2 = bate2.move(0, -5)

    ventana.fill((252, 243, 207))
    ventana.blit(ball, ballrect)
    pygame.draw.rect(ventana, ROJO, bate1, 0)
    pygame.draw.rect(ventana, NEGRO, bate2, 0)

    scores = FONT.render(f'{cont_bate1}          {cont_bate2}', True, NEGRO)
    ventana.blit(scores, (ventana.get_width() / 2 - scores.get_width() / 2, 20))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()