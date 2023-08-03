import pygame

from jogador import Jogador

class Objetivo(Jogador):
    def __init__(self, x, y, fase_atual):
        super().__init__(x, y, fase_atual)
        self.image = pygame.Surface((30, 40))
        self.image_color = self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.fase_atual = fase_atual