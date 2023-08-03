import pygame

from constantes import *
from jogador import *
from objetivo import *
from plataforma import *
from funcoes import adicionar, gerar_texto

jogador_group = pygame.sprite.Group()
plataforma_group = pygame.sprite.Group()
objetivo_group = pygame.sprite.Group()

hud = Plataforma(0, 0, 640, 50, (25,25,25))
plataforma_direita = Plataforma(-1, 0, 1, 480, CINZA)
plataforma_baixo = Plataforma(0, 480, 640, 1, CINZA)
plataforma_esquerda = Plataforma(640, 0, 1, 480, CINZA)

mapa = [hud, plataforma_direita, plataforma_esquerda, plataforma_baixo]

adicionar(mapa, plataforma_group)

def fase2():
     
     plataforma_group.draw(tela)

     gerar_texto("Level 2", "white", 251, 30)

     return 2