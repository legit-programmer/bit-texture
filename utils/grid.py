import pygame

class Grid:
    def __init__(self, window:pygame.Surface, dimensionsInPixels:tuple) -> None:
        self.col, self.row = (8, 8)
        self.WIN = window
        self.WIDTH, self.HEIGHT = dimensionsInPixels

    def getGridPos(self, pixelsPos: tuple):
        return (int(pixelsPos[0]/(self.WIDTH/self.col)), int(pixelsPos[1]/(self.HEIGHT/self.row)))

    def drawGrid(self):
        for i in range(self.col+1):
            pygame.draw.line(self.WIN, (0, 0, 0), (i*(self.WIDTH/self.col), 0),
                             (i*(self.WIDTH/self.col), self.HEIGHT))

        for j in range(self.row):
            pygame.draw.line(self.WIN, (0, 0, 0), (0, j*(self.HEIGHT/self.row)),
                             (self.WIDTH, j*(self.HEIGHT/self.row)))

    def get_grid(self):
        return (self.col, self.row)

    def set_grid(self, col, row):
        self.WIN.fill((255, 255, 255))
        self.col, self.row = col, row