import pygame

from funcoes import gerar_texto
from constantes import *

def final(tempo):
    pygame.mixer.music.stop()

    gerar_texto("Parabéns!", AMARELO, 150, 80, 40)
    gerar_texto(f"Seu tempo foi de {tempo} segundos", BRANCO, 15, 220, 20)
    gerar_texto("Tempo adicionado!", BRANCO, 70, 340, 30)

    return 5