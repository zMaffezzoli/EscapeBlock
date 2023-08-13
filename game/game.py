import pygame

from fase1 import *
from fase2 import *
from fase3 import *
from final import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load('./game/assets/sound/beat_music.mp3')
        pygame.mixer.music.play(-1)
        
        self.run = True
        self.fase_atual = 1

    def fases(self):
        if self.fase_atual == 1:
            self.fase_atual = fase1()
        
        elif self.fase_atual == 2:
            self.fase_atual = fase2()

        elif self.fase_atual == 3:
            self.fase_atual = fase3()

        elif self.fase_atual == 4:
            final()

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