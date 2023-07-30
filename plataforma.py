import pygame
from constantes import *

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image_color = self.image.fill(cor)
        self.rect = self.image.get_rect(topleft=(x, y))

plataforma_group = pygame.sprite.Group()