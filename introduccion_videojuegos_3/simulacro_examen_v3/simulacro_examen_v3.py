import pygame
from os import *
from random import *

#Inicilización de Pygame
pygame.init()

ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

FONT = pygame.font.Font(None, 40)

#Inicialización de la superficie de dibujo
WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

#Titulo del juego
pygame.display.set_caption("Simulacro Examen 3")

ball = pygame.image.load("introduccion_videojuegos/ejemplo4/assets/imgs/ball.png")
ball = pygame.transform.scale(ball, (40, 40))
ballrect = ball.get_rect()
speed = [randint(3, 6), randint(3, 6)]
ballrect.move_ip(0, 200)

bate = pygame.Rect((WIDTH / 2) - 100 , HEIGHT - 49, 150, 20)

ladrillos = []
dimensiones_ladrillo = [WIDTH / 12, HEIGHT / 12]

y = 10
for i in range(3):
    x = 10
    ladrillos_fila = []
    for j in range(10):
        ladrillos_fila.append(pygame.Rect(x, y, dimensiones_ladrillo[0], dimensiones_ladrillo[1]))
        x = x + dimensiones_ladrillo[0] + 10
    ladrillos.append(ladrillos_fila)
    y = y + dimensiones_ladrillo[1] + 10

#Bucle principal del juego
run = True
menu = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        bate = bate.move(-5, 0)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        bate = bate.move(5, 0)
    
    if bate.left < 0:
        bate = bate.move(5, 0)
    elif bate.right > ventana.get_width():
        bate = bate.move(-5, 0)
    
    ballrect = ballrect.move(speed)

    if bate.colliderect(ballrect):
        speed[1] = -speed[1]

    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    if ballrect.bottom > ventana.get_height():
        menu = True
        menu_bkg = pygame.Rect((0, 0, WIDTH, HEIGHT))
        pygame.draw.rect(ventana, NEGRO, menu_bkg)
        resultado = FONT.render("You Lose",True, ROJO)
        speed[0] = 0
        speed[1] = 0

    if len(ladrillos) < 1:
        menu = True
        menu_bkg = pygame.Rect((0, 0, WIDTH, HEIGHT))
        pygame.draw.rect(ventana, NEGRO, menu_bkg)
        resultado = FONT.render("You Win", True, ROJO)
        speed[0] = 0
        speed[1] = 0

    if not menu:
        ventana.fill((252, 243, 207))
        
        for fila in ladrillos:
            for ladrillo in fila:
                pygame.draw.rect(ventana, ROJO, ladrillo)
                if ballrect.colliderect(ladrillo):
                    speed[1] = -speed[1]
                    fila.remove(ladrillo)
                    if len(fila) == 0:
                        ladrillos.remove(fila)
        
        ventana.blit(ball, ballrect)
        pygame.draw.rect(ventana, NEGRO, bate, 0)
    else: 
        ventana.blit(resultado, (menu_bkg.centerx - resultado.get_width() / 2, menu_bkg.centery - resultado.get_height() / 2 - 20))
        txtSalir = FONT.render("Pulsa 'Q' para salir", True, ROJO)
        ventana.blit(txtSalir, (menu_bkg.centerx - txtSalir.get_width() / 2, menu_bkg.centery - txtSalir.get_height() / 2 + 20))
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()