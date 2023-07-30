import pygame

from constantes import *
from jogador import *
from plataforma import *
from texto import *

jogador = Jogador(30,420)
jogador_group.add(jogador)

hud = Plataforma(0, 0, 640, 50, (25, 25, 25))
plataforma_baixo = Plataforma(0, 480, 640, 1, (0, 255 ,0))
plataforma_direita = Plataforma(-1, 0, 1, 480, (0, 255 ,0))
plataforma_esquerda = Plataforma(640, 0, 1, 480, (0, 255 ,0))

#plataforma(x, y, largura, altura, cor)
l1 = Plataforma(240, 50, 10, 80, (255, 255, 255))
l2 = Plataforma(380, 50, 10, 90, (255, 255, 255))
l3 = Plataforma(300, 140, 170, 10, (255, 255, 255))
l4 = Plataforma(540, 150, 100, 10, (255, 255, 255))
l5 = Plataforma(540, 100, 10, 50, (255, 255, 255))
l6 = Plataforma(550, 100, 50, 10, (255, 255, 255))
l7 = Plataforma(300, 140, 10, 60, (255, 255, 255))
l8 = Plataforma(470, 140, 10, 70, (255, 255, 255))
l9 = Plataforma(400, 210, 120, 10, (255, 255, 255))
l10 = Plataforma(400, 220, 10, 70, (255, 255, 255))
l11 = Plataforma(300, 290, 110, 10, (255, 255, 255))
l12 = Plataforma(300, 290, 10, 80, (255, 255, 255))
l13 = Plataforma(200, 370, 110, 10, (255, 255, 255))
l14 = Plataforma(400, 360, 10, 120, (255, 255, 255))
l15 = Plataforma(300, 380, 10, 60, (255, 255, 255))
l16 = Plataforma(510, 220, 10, 80, (255, 255, 255))
l17 = Plataforma(510, 350, 10, 60, (255, 255, 255))
l18 = Plataforma(470, 410, 100, 10, (255, 255, 255))
l19 = Plataforma(580, 300, 60, 10, (255, 255, 255))
l20 = Plataforma(580, 220, 10, 80, (255, 255, 255))

plataforma_group.add(plataforma_baixo)
plataforma_group.add(plataforma_direita)
plataforma_group.add(plataforma_esquerda)
plataforma_group.add(hud)
plataforma_group.add(l1)
plataforma_group.add(l2)
plataforma_group.add(l3)
plataforma_group.add(l4)
plataforma_group.add(l5)
plataforma_group.add(l6)
plataforma_group.add(l7)
plataforma_group.add(l8)
plataforma_group.add(l9)
plataforma_group.add(l10)
plataforma_group.add(l11)
plataforma_group.add(l12)
plataforma_group.add(l13)
plataforma_group.add(l14)
plataforma_group.add(l15)
plataforma_group.add(l16)
plataforma_group.add(l17)
plataforma_group.add(l18)
plataforma_group.add(l19)
plataforma_group.add(l20)

def fase1():

    jogador_group.update()
    jogador_group.draw(tela)

    plataforma_group.draw(tela)

    gerar_texto("Level 1", "white", 251, 30)