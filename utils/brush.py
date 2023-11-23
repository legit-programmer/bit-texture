import pygame
from .grid import Grid


class Brush:
    def __init__(self, window: pygame.Surface, gridDimension: tuple, color: tuple) -> None:
        self.color = color
        self.WIN = window
        self.WIDTH, self.HEIGHT = gridDimension
        self.transparent = False
        self.disabled = False
        

    def draw(self, grid: Grid, gridPos: tuple):
        if gridPos[0] < grid.get_grid()[0] and gridPos[1] < grid.get_grid()[1] and not self.disabled:
            left = gridPos[0]*(self.WIDTH/grid.get_grid()[0])
            top = gridPos[1]*(self.HEIGHT/grid.get_grid()[1])
            width = self.WIDTH/grid.get_grid()[0]+1
            height = self.HEIGHT/grid.get_grid()[1]+1
            if self.transparent:
                self.color = (0, 1, 0)
            pygame.draw.rect(self.WIN, self.color, pygame.Rect(
                left, top, width, height))

            
                

    def setColor(self, color: tuple):
        self.transparent = False
        self.color = color

    def setTransparent(self, value:bool):
        self.transparent = value
