import pygame
from constantes import TELA

def adicionar(objetos, group):
    for x in objetos:
        group.add(x)

def gerar_texto(texto, cor, x, y, tamanho):
    font = pygame.font.Font("./game/assets/font/8-bit_font.ttf", tamanho)
    img = font.render(texto, False, cor)
    TELA.blit(img, (x, y))