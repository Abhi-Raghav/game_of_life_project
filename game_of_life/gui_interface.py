import pygame
import game_engine as ge


pygame.init()

# Defining constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

GRID_SIZE = (40, 40)
CELL_SIZE = (SCREEN_WIDTH/GRID_SIZE[0], SCREEN_HEIGHT/GRID_SIZE[1])



class Cell(pygame.sprite.Sprite):
    def __init__(self, cell_value):
        super(Cell, self).__init__()
        self.surf = pygame.Surface(CELL_SIZE)
        if cell_value == 1: # alive
            self.surf.fill((0, 0, 0))
        else:   # dead
            self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


