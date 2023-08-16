import pygame

#Dimensões da tela
LARGURA = 640
ALTURA = 480

#Definindo tela
TELA = pygame.display.set_mode((LARGURA, ALTURA))

#Definindo título do jogo
TITULO_JOGO = "EscapeBlock"
pygame.display.set_caption(TITULO_JOGO)

#Definindo FPS do jogo
FPS = 60
CLOCK = pygame.time.Clock()

#Cores
CINZA = (2, 2, 2)
PRETO = (0, 0, 0)
AMARELO = (255, 215, 0)
BRANCO = (200, 200, 200)
VERDE = (0, 80, 0)
AZUL = (0, 0, 255)

PLAYER = ""