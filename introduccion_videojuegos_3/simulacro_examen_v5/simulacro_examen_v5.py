import pygame
from os import *
import random
import time

#Inicilización de Pygame
pygame.init()

#Inicialización de la superficie de dibujo
WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

#Titulo del juego
pygame.display.set_caption("Simumlacro examen 5")

ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
GRIS = (58, 58, 58)

FONT = pygame.font.Font(None, 40)

cabeza = pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20)
speed = [0, 0]

comida = pygame.Rect(100, 100, 18, 18)

segmentos = []

#Bucle principal del juego
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed[0] = -3
                speed[1] = 0
            if event.key == pygame.K_d:
                speed[0] = 3
                speed[1] = 0
            if event.key == pygame.K_w:
                speed[1] = -3
                speed[0] = 0
            if event.key == pygame.K_s:
                speed[1] = 3
                speed[0] = 0

    if cabeza.left < 0 or cabeza.right > ventana.get_width():
        speed = [0, 0]
        cabeza.x = (WIDTH / 2 - 10)
        cabeza.y = (HEIGHT / 2 - 10)
        for element in segmentos:
            element.x = -50
            element.y = -50
        segmentos.clear()
        
    if cabeza.top < 0 or cabeza.bottom > ventana.get_height():
        speed = [0, 0]
        cabeza.x = (WIDTH / 2 - 10)
        cabeza.y = (HEIGHT / 2 - 10)
        for element in segmentos:
            element.x = -50
            element.y = -50
        segmentos.clear()

    if cabeza.colliderect(comida):
        x = random.randint(18, WIDTH - 18)
        y = random.randint(18, HEIGHT - 18)
        comida.x = x
        comida.y = y
        nuevo_segmento = pygame.Rect(0, 0, 20, 20)
        segmentos.append(nuevo_segmento)

    cabeza = cabeza.move(speed)
    
    ventana.fill((252, 243, 207))

    pygame.draw.rect(ventana, NEGRO, cabeza, 0)
    pygame.draw.rect(ventana, ROJO, comida, 0)

    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].x
        y = segmentos[index - 1].y
        if speed[0] > 0:
            segmentos[index].x = x - cabeza.width
            segmentos[index].y = y
        elif speed[0] < 0:
            segmentos[index].x = x + cabeza.width
            segmentos[index].y = y 
        elif speed[1] > 0:
            segmentos[index].x = x
            segmentos[index].y = y - cabeza.height
        elif speed[1] < 0: 
            segmentos[index].x = x
            segmentos[index].y = y + cabeza.height
        pygame.draw.rect(ventana, GRIS, segmentos[index], 0)
    
    if totalSeg > 0:
        x = cabeza.x
        y = cabeza.y
        segmentos[0].x = x
        segmentos[0].y = y
    
    
    # for segmento in segmentos:
    #     if cabeza.colliderect(segmento):
    #         speed = [0, 0]
    #         cabeza.x = (WIDTH / 2 - 10)
    #         cabeza.y = (HEIGHT / 2 - 10)
    #         for element in segmentos:
    #             element.x = -50
    #             element.y = -50
    #         segmentos.clear()
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()