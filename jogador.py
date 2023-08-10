import pygame

from groups import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y, fase_atual):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image_color = self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.fase_atual = fase_atual

    def mover(self, pk):
        if self.fase_atual != 2:
            if pk[pygame.K_a]:
                self.rect.x -= 1
            if pk[pygame.K_d]:
                self.rect.x += 1
            if pk[pygame.K_w]:
                self.rect.y -= 1
            if pk[pygame.K_s]:
                self.rect.y += 1
            
    def salvar_xy(self):
        self.antes_x = self.rect.x
        self.antes_y = self.rect.y

    def restaurar_xy(self):
        self.rect.x = self.antes_x
        self.rect.y = self.antes_y
    
    def update(self):
        self.salvar_xy()
        teclas = pygame.key.get_pressed()
        self.mover(teclas)

        collided = pygame.sprite.spritecollide(self, plataforma_group, False)
        if collided:
            self.restaurar_xy()

        venceu = pygame.sprite.spritecollide(self, objetivo_group, True)
        if venceu:
            plataforma_group.empty()
            objetivo_group.empty()
            jogador_group.empty()
            self.fase_atual += 1