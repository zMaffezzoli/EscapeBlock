import pygame

from game import Game

GAME = Game()

while GAME.run:
    
    GAME.update()

pygame.quit()