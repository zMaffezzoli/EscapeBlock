import pygame

from constantes import *
from jogador import *
from objetivo import *
from plataforma import *
from groups import *
from funcoes import adicionar, gerar_texto

#jogador = Jogador(30,420)
jogador = Jogador(577,61)
jogador_group.add(jogador)

objetivo = Objetivo(580, 100)
objetivo_group.add(objetivo)

hud = Plataforma(0, 0, 640, 50, (25,25,25))
plataforma_direita = Plataforma(-1, 0, 1, 480, CINZA)
plataforma_baixo = Plataforma(0, 480, 640, 1, CINZA)
plataforma_esquerda = Plataforma(640, 0, 1, 480, CINZA)
l1 = Plataforma(240, 50, 10, 80, CINZA)
l2 = Plataforma(380, 50, 10, 90, CINZA)
l3 = Plataforma(300, 140, 170, 10, CINZA)
l4 = Plataforma(540, 150, 100, 10, CINZA)
l5 = Plataforma(540, 100, 10, 50, CINZA)
l6 = Plataforma(0, 150, 70, 10, CINZA)
l7 = Plataforma(300, 140, 10, 60, CINZA)
l8 = Plataforma(470, 140, 10, 70, CINZA)
l9 = Plataforma(400, 210, 120, 10, CINZA)
l10 = Plataforma(400, 220, 10, 70, CINZA)
l11 = Plataforma(300, 290, 110, 10, CINZA)
l12 = Plataforma(300, 290, 10, 80, CINZA)
l13 = Plataforma(200, 370, 110, 10, CINZA)
l14 = Plataforma(400, 360, 10, 120, CINZA)
l15 = Plataforma(300, 380, 10, 60, CINZA)
l16 = Plataforma(510, 220, 10, 80, CINZA)
l17 = Plataforma(510, 350, 10, 60, CINZA)
l18 = Plataforma(470, 410, 100, 10, CINZA)
l19 = Plataforma(580, 300, 60, 10, CINZA)
l20 = Plataforma(580, 220, 10, 80, CINZA)
l21 = Plataforma(120, 300, 10, 180, CINZA)
l22 = Plataforma(70, 300, 140, 10, CINZA)
l23 = Plataforma(200, 220, 10, 80, CINZA)
l24 = Plataforma(70, 220, 140, 10, CINZA)
l25 = Plataforma(150, 150, 10, 70, CINZA)

mapa = [hud, plataforma_direita, plataforma_esquerda, plataforma_baixo, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14,l15, l16, l17, l18, l19,l20, l21, l22, l23, l24, l25]

adicionar(mapa, plataforma_group)

def fase1():

    jogador_group.draw(tela)

    plataforma_group.draw(tela)

    objetivo_group.draw(tela)

    gerar_texto("Level 1", "white", 251, 30)
    
    jogador_group.update()