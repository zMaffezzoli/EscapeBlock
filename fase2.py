import pygame

from constantes import *
from jogador import *
from objetivo import *
from plataforma import *
from funcoes import adicionar, gerar_texto
from groups import *

jogador = Jogador(577, 61, 2)

objetivo = Objetivo(580, 100, 2)

hud = Plataforma(0, 0, 640, 50, (25,25,25))
plataforma_direita = Plataforma(-1, 0, 1, 480, CINZA)
plataforma_baixo = Plataforma(0, 480, 640, 1, CINZA)
plataforma_esquerda = Plataforma(640, 0, 1, 480, CINZA)

mapa = [hud, plataforma_direita, plataforma_esquerda, plataforma_baixo]

def fase2():
     
     adicionar(mapa, plataforma_group)
     plataforma_group.draw(tela)

     jogador_group.add(jogador)
     jogador_group.draw(tela)

     objetivo_group.add(objetivo)
     objetivo_group.draw(tela)
     objetivo_group.update()

     gerar_texto("Level 2", "white", 251, 30, 20)

     return objetivo.fase_atual