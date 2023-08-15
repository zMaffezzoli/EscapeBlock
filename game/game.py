import pygame

from fase1 import *
from fase2 import *
from fase3 import *
from final import *
from cronometro import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load('./game/assets/sound/beat_music.mp3')
        pygame.mixer.music.play(-1)
        
        self.run = True
        self.fase_atual = 1
        self.cronometro = Cronometro()
        self.tempo = None

    def fases(self):
        if self.fase_atual == 1:
            self.fase_atual = fase1(self.tempo)
        
        elif self.fase_atual == 2:
            self.fase_atual = fase2(self.tempo)

        elif self.fase_atual == 3:
            self.fase_atual = fase3(self.tempo)

        elif self.fase_atual == 4:
            final(self.tempo)

    def salvar_tempo(self):
        if self.fase_atual != 4:
            self.tempo = self.cronometro.obter_tempo()

    def sair(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self):
        
        clock.tick(FPS)
        
        tela.fill("black")

        self.fases()
        self.salvar_tempo()

        self.sair()

        pygame.display.flip()