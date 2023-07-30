import pygame

from constantes import *
from funcoes import *
from fase1 import *

pygame.init()

run = True
while run:
    clock.tick(FPS)

    tela.fill("black")
    
    sair()

    fase1()

    pygame.display.update()