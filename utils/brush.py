import pygame
from .grid import Grid

class Brush:
    def __init__(self, window:pygame.Surface, gridDimension:tuple, color: tuple) -> None:
        self.color = color
        self.WIN = window
        self.WIDTH, self.HEIGHT = gridDimension

    def draw(self, grid: Grid, gridPos: tuple):
        if gridPos[0] < grid.get_grid()[0] and gridPos[1] < grid.get_grid()[1]:
            pygame.draw.rect(self.WIN, self.color, pygame.Rect(
                gridPos[0]*(self.WIDTH/grid.get_grid()[0]), gridPos[1]*(self.HEIGHT/grid.get_grid()[1]), self.WIDTH/grid.get_grid()[0]+2, self.HEIGHT/grid.get_grid()[1]+2))

    def setColor(self, color: tuple):
        self.color = color