import pygame
from ui import Components, ClickListener
from utils.grid import Grid
from utils.brush import Brush

pygame.init()

WIDTH, HEIGHT = (800, 800)
WIN_WIDTH, WIN_HEIGHT = (1280, 800)
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()

running = True
WIN.fill((255, 255, 255))


grid = Grid(WIN, (WIDTH, HEIGHT))
component = Components(WIN)
clickListener = ClickListener()
brush = Brush(WIN, (WIDTH, HEIGHT), (255, 0, 0))

eraser = component.Button('eraser')
clear = component.Button('clear')

green = component.Button('green')
red = component.Button('red')
blue = component.Button('blue')
yellow = component.Button('yellow')

bit8 = component.Button('8x8')
bit16 = component.Button('16x16')
bit32 = component.Button('32x32')
bit64 = component.Button('64x64')
bit128 = component.Button('128x128')


clickListener.addListener(eraser, lambda: brush.setColor((255, 255, 255)))
clickListener.addListener(clear, lambda: WIN.fill((255, 255, 255)))


clickListener.addListener(green, lambda: brush.setColor((0, 255, 0)))
clickListener.addListener(red, lambda: brush.setColor((255, 0, 0)))
clickListener.addListener(yellow, lambda: brush.setColor((255, 255, 0)))
clickListener.addListener(blue, lambda: brush.setColor((0, 0, 255)))

clickListener.addListener(bit16, lambda: grid.set_grid(16, 16))
clickListener.addListener(bit32, lambda: grid.set_grid(32, 32))
clickListener.addListener(bit64, lambda: grid.set_grid(64, 64))
clickListener.addListener(bit128, lambda: grid.set_grid(128, 128))
clickListener.addListener(bit8, lambda: grid.set_grid(8, 8))
while running:

    grid.drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    left, middle, right = pygame.mouse.get_pressed()
    if left:
        grid_position = grid.getGridPos(pygame.mouse.get_pos())
        brush.draw(grid, grid_position)

    component.drawAllComponents()

    clickListener.listenEvents()
    pygame.display.flip()
    CLOCK.tick(FPS)
