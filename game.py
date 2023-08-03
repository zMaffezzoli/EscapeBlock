import pygame

from fase1 import *

class Game:
    def __init__(self):
        pygame.init()
        self.run = True

    def fases(self):
        global FASE
        if FASE == 1:
            fase1()
        
        elif FASE == 2:
            print("fase 2")