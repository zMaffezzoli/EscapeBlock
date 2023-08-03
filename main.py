import pygame

from constantes import *
from funcoes import *
from game import Game

g = Game()

while g.run:
    clock.tick(FPS)

    tela.fill("black")

    g.fases()

    sair()
    pygame.display.flip()