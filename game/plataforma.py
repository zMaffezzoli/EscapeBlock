import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor):
        super().__init__()
        self.image = pygame.Surface((largura, altura), pygame.SRCALPHA)
        self.image_color = self.image.fill(cor)
        self.rect = self.image.get_rect(topleft=(x, y))