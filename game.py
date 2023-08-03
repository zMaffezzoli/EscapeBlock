import pygame

from fase1 import *

class Game:
    def __init__(self):
        pygame.init()
        self.run = True
        self.fase_atual = 1

    def fases(self):
        if self.fase_atual == 1:
            self.fase_atual = fase1()
        
        elif self.fase_atual == 2:
            print("fase 2")

        elif self.fase_atual == 3:
            print("fase 3")

    def sair(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self):

        clock.tick(FPS)

        tela.fill("black")

        self.fases()

        self.sair()
        
        pygame.display.flip()