import pygame
from constantes import tela
from sys import exit

def sair():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
def adicionar(objetos, group):
    for x in objetos:
        group.add(x)

def gerar_texto(texto, cor, x, y):
    font = pygame.font.Font("./assets/8-bit_font.ttf", 20)
    img = font.render(texto, False, cor)
    tela.blit(img, (x, y))