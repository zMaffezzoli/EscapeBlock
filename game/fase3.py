import pygame

from constantes import *
from jogador import *
from objetivo import *
from plataforma import *
from funcoes import adicionar, gerar_texto
from groups import *

jogador = Jogador((LARGURA-30)/2, 350, 3)

objetivo = Objetivo(500, 200, 3)

hud = Plataforma(0, 0, 640, 50, (25,25,25))
plataforma_direita = Plataforma(-1, 0, 1, 480, PRETO)
plataforma_baixo = Plataforma(0, 480, 640, 1, PRETO)
plataforma_esquerda = Plataforma(640, 0, 1, 480, PRETO)
r1 = Plataforma(133, 200, 30, 40, AZUL)
r2 = Plataforma(316, 200, 30, 40, AZUL)

mapa = [hud, plataforma_direita, plataforma_esquerda, plataforma_baixo, r1, r2]

def fase3():

    adicionar(mapa, plataforma_group)
    plataforma_group.draw(tela)

    jogador_group.add(jogador)
    jogador_group.draw(tela)
    jogador_group.update()

    objetivo_group.add(objetivo)
    objetivo_group.draw(tela)

    gerar_texto("Level 3", AMARELO, 251, 30, 20)
    gerar_texto("Anteontem era quarta, há 17 dias era?", BRANCO, 100, 10, 12)
    gerar_texto("Domingo         Quarta          Terça", BRANCO, 105, 185, 12)

    return jogador.fase_atual