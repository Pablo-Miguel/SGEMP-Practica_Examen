import pygame
from os import *

#Inicilización de Pygame
pygame.init()

#Inicialización de la superficie de dibujo
WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

#Titulo del juego
pygame.display.set_caption("Ejemplo 1")

#Bucle principal del juego
run = True

while run:
    #Comprobamos los eventos
    #Comprobamos si se ha pulsado el botón de cierre la ventana
    #Pygame event.get() recorre una lista de eventos como puede ser pulsar teclas, darle click al ratón, etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            #Se pinta la ventana con un color
            #Esto borra los posibles elementos que teníamos anteriormente
            ventana.fill((252, 243, 207))
            #Todos los elementos del juego se vuelven a dibujar
            pygame.display.flip()
            #Controlamos la frecuencia de refresco (FPS)
            pygame.time.Clock().tick(60)

pygame.quit()