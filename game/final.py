import pygame

from funcoes import gerar_texto
from constantes import *

def final(tempo):
    pygame.mixer.music.stop()

    gerar_texto("Parabéns!", AMARELO, 150, 50, 40)
    gerar_texto(f"Seu tempo foi de {tempo} segundos", BRANCO, 15, 150, 20)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            PLAYER += event.unicode

    print(PLAYER)