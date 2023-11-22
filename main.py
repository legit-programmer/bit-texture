import pygame
import random
from ui import Components, ClickListener

pygame.init()

WIDTH, HEIGHT = (800, 800)
WIN_WIDTH, WIN_HEIGHT = (1280, 800)
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()

running = True
WIN.fill((255, 255, 255))


class Brush:
    def __init__(self, color: tuple) -> None:
        self.color = color

    def draw(self, grid: tuple, gridPos: tuple):
        if gridPos[0] < grid[0] and gridPos[1] < grid[1]:
            pygame.draw.rect(WIN, self.color, pygame.Rect(
                gridPos[0]*(WIDTH/grid[0]), gridPos[1]*(HEIGHT/grid[1]), WIDTH/grid[0]+2, HEIGHT/grid[1]+2))

    def setColor(self, color: tuple):
        self.color = color


def getGridPos(pixelsPos: tuple, grid: tuple):
    return (int(pixelsPos[0]/(WIDTH/grid[0])), int(pixelsPos[1]/(HEIGHT/grid[1])))


def drawGrid(col: int, row: int):
    for i in range(col):
        pygame.draw.line(WIN, (0, 0, 0), (i*(WIDTH/col), 0),
                         (i*(WIDTH/col), HEIGHT))

    for j in range(row):
        pygame.draw.line(WIN, (0, 0, 0), (0, j*(HEIGHT/row)),
                         (WIDTH, j*(HEIGHT/row)))

    return (col, row)


component = Components(WIN)
clickListener = ClickListener()
brush = Brush((255, 0, 0))

eraser = component.Button('eraser')
green = component.Button('green')
red = component.Button('red')
blue = component.Button('blue')
yellow = component.Button('yellow')

clickListener.addListener(eraser, lambda: brush.setColor((255, 255, 255)))
clickListener.addListener(green, lambda: brush.setColor((0, 255, 0)))
clickListener.addListener(red, lambda: brush.setColor((255, 0, 0)))
clickListener.addListener(yellow, lambda: brush.setColor((255, 255, 0)))
clickListener.addListener(blue, lambda: brush.setColor((0, 0, 255)))

while running:

    grid = drawGrid(8, 8)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    left, middle, right = pygame.mouse.get_pressed()
    if left:
        grid_position = getGridPos(pygame.mouse.get_pos(), grid)
        brush.draw(grid, grid_position)

    component.drawAllComponents()

    clickListener.listenEvents()
    pygame.display.flip()
    CLOCK.tick(FPS)
