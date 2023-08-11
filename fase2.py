import pygame

from constantes import *
from jogador import *
from objetivo import *
from plataforma import *
from funcoes import adicionar, gerar_texto
from groups import *

jogador = Jogador(35, 230, 2)

#objetivo = Objetivo(575, 420, 2)
objetivo = Objetivo(35, 270, 2)

hud = Plataforma(0, 0, 640, 50, (25,25,25))
plataforma_direita = Plataforma(-1, 0, 1, 480, PRETO)
plataforma_baixo = Plataforma(0, 480, 640, 1, PRETO)
plataforma_esquerda = Plataforma(640, 0, 1, 480, PRETO)
l1 = Plataforma(100, 50, 440, 61, VERDE)
l2 = Plataforma(100, 419, 440, 61, VERDE)
l3 = Plataforma(440, 173, 100, 61, VERDE)
l4 = Plataforma(440, 296, 100, 61, VERDE)
l5 = Plataforma(100, 173, 100, 61, VERDE)
l6 = Plataforma(100, 296, 100, 61, VERDE)
l7 = Plataforma(285, 173, 70, 61, VERDE)
l8 = Plataforma(285, 296, 70, 61, VERDE)
l9 = Plataforma(440, 234, 1, 62, PRETO)
l10 = Plataforma(440, 357, 1, 62, PRETO)
l11 = Plataforma(285, 234, 1, 62, PRETO)
l12 = Plataforma(285, 111, 1, 62, PRETO)
l13 = Plataforma(100, 111, 1, 62, PRETO)
l14 = Plataforma(100, 357, 1, 62, PRETO)
mapa = [hud, plataforma_direita, plataforma_esquerda, plataforma_baixo, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14]

def fase2():
     
     adicionar(mapa, plataforma_group)
     plataforma_group.draw(tela)

     jogador_group.add(jogador)
     jogador_group.draw(tela)

     objetivo_group.add(objetivo)
     objetivo_group.draw(tela)
     objetivo_group.update()

     gerar_texto("Level 2", AMARELO, 251, 30, 20)

     gerar_texto("Nao seGuimos PadRoes", BRANCO, 200, 10, 12)

     return objetivo.fase_atual