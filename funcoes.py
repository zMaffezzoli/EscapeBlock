import pygame
from constantes import tela

def adicionar(objetos, group):
    for x in objetos:
        group.add(x)

def gerar_texto(texto, cor, x, y, tamanho):
    font = pygame.font.Font("./assets/8-bit_font.ttf", tamanho)
    img = font.render(texto, False, cor)
    tela.blit(img, (x, y))