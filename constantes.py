import pygame

#Dimensões da tela
LARGURA = 640
ALTURA = 480

#Definindo tela
tela = pygame.display.set_mode((LARGURA, ALTURA))

#Definindo título do jogo
TITULO_JOGO = "EscapeBlock"
pygame.display.set_caption(TITULO_JOGO)

#Definindo FPS do jogo
FPS = 60
clock = pygame.time.Clock()

CINZA = (255, 255, 255)
#CINZA = (4, 4, 4)

FASE = 1