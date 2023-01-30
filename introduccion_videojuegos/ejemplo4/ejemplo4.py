import pygame
from random import *
from os import *

pygame.init()

WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Ejemplo 4")

bg = pygame.image.load("introduccion_videojuegos/ejemplo4/assets/imgs/bg.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

ball = pygame.image.load("introduccion_videojuegos/ejemplo4/assets/imgs/ball.png")
ball = pygame.transform.scale(ball, (40, 40))
ballrect = ball.get_rect()

#La velocidad se calcula con un valor pseudialeatorio entre 3,6
speed = [randint(3, 6), randint(3, 6)]
ballrect.move_ip(0,0)

bate = pygame.image.load("introduccion_videojuegos/ejemplo4/assets/imgs/bate.png")
bate = pygame.transform.scale(bate, (100, 49))
baterect = bate.get_rect()
baterect.move_ip((WIDTH / 2) - bate.get_width() , HEIGHT - bate.get_height())

#Esta es la fuente que usaremos para el texto que aparecerá en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)

texto = ""
texto_rect = None
game_over = False

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        baterect = baterect.move(-3, 0)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        baterect = baterect.move(3, 0)

    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
        #Si la pelota toca abajo
        if ballrect.bottom > ventana.get_height():
            texto = fuente.render("Game Over -> Space para salir...", True, (125, 125, 125))
            texto_rect = texto.get_rect()
            texto_rect.center = (WIDTH / 2, HEIGHT / 2)
            game_over = True

    ventana.fill((255, 105, 180))
    ventana.blit(bg, (0,0))
    ventana.blit(ball, ballrect)
    ventana.blit(bate, baterect)
    if game_over:
        speed[0] = 0
        speed[1] = 0
        ballrect.center = (WIDTH / 2, HEIGHT / 2)
        ventana.fill((0, 0, 0))
        ventana.blit(texto, texto_rect)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            run = False
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()