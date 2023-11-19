import pygame
import os

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

#Fundo
arquivo = os.path.dirname(os.path.abspath(__file__))
pasta = os.path.join(arquivo, "img/")
imagem = os.path.join(pasta, "background.png")
background = pygame.image.load(imagem)

#Cores
CINZA = (4, 4, 4)
PRETO = (0, 0, 0)
AMARELO = (255, 215, 0)
BRANCO = (200, 200, 200)
VERDE = (0, 80, 0)
AZUL = (0, 0, 255)

#Definindo URL para enviar o tempo
URL = "http://localhost:5000/incluir/Jogada"