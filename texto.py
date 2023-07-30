import pygame
from constantes import tela

#Use esta variavel para definir a fonte!

#Função para gerar textos
def gerar_texto(texto, cor, x, y):
    font = pygame.font.Font("./assets/8-bit_font.ttf", 20)
    img = font.render(texto, False, cor)
    tela.blit(img, (x, y))