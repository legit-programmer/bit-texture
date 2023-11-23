import pygame
from ui import Components, ClickListener
from utils.grid import Grid
from utils.brush import Brush
import os
import numpy as np
from PIL import Image, ImageDraw, ImageDraw2
pygame.init()

WIDTH, HEIGHT = (800, 800)
WIN_WIDTH, WIN_HEIGHT = (1280, 800)
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 18)
running = True
WIN.fill((255, 255, 255))


grid = Grid(WIN, (WIDTH, HEIGHT))
component = Components(WIN)
clickListener = ClickListener()
brush = Brush(WIN, (WIDTH, HEIGHT), (255, 0, 0))

eraser = component.Button('eraser')
transparent = component.Button('Transperant')
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

export = component.Button('export')
exporting = False




def checkColor():
    keys = pygame.key.get_pressed()
    R, G, B = brush.color
    print(B)
    text = f'RED: {R}, GREEN: {G}, BLUE: {B}'
    text = font.render(text, False, (255, 255, 255), (0, 0, 255))
    WIN.blit(text, (980, 10))
    
    if keys[pygame.K_r] and keys[pygame.K_UP] and R < 255:
        brush.setColor((R+1, G, B))

    if keys[pygame.K_r] and keys[pygame.K_DOWN] and R > 0:
        brush.setColor((R-1, G, B))

    if keys[pygame.K_g] and keys[pygame.K_UP] and G < 255:
        brush.setColor((R, G+1, B))

    if keys[pygame.K_g] and keys[pygame.K_DOWN] and G > 0:
        brush.setColor((R, G-1, B))

    if keys[pygame.K_b] and keys[pygame.K_UP] and B < 255:
        brush.setColor((R, G, B+1))

    if keys[pygame.K_b] and keys[pygame.K_DOWN] and B > 0:
        brush.setColor((R, G, B-1))


def exportBuffer():
    global exporting
    if not exporting:

        image = Image.new('RGBA', grid.get_grid())
        draw = ImageDraw.Draw(image)
        for i in range(0, grid.get_grid()[0]):
            for j in range(0, grid.get_grid()[1]):

                R, G, B, A = WIN.get_at(
                    (int((i*(WIDTH/grid.get_grid()[0]))+1), int((j*(HEIGHT/grid.get_grid()[1]))+1)))

                if (R, G, B) != (0, 1, 0):
                    draw.point((i, j), (R, G, B, A))

        image.save('export.png')
        exporting = False


clickListener.addListener(eraser, lambda: brush.setColor((255, 255, 255)))
clickListener.addListener(clear, lambda: WIN.fill((255, 255, 255)))

clickListener.addListener(export, exportBuffer)
clickListener.addListener(green, lambda: brush.setColor((0, 255, 0)))
clickListener.addListener(red, lambda: brush.setColor((255, 0, 0)))
clickListener.addListener(yellow, lambda: brush.setColor((255, 255, 0)))
clickListener.addListener(blue, lambda: brush.setColor((0, 0, 255)))

clickListener.addListener(bit16, lambda: grid.set_grid(16, 16))
clickListener.addListener(bit32, lambda: grid.set_grid(32, 32))
clickListener.addListener(bit64, lambda: grid.set_grid(64, 64))
clickListener.addListener(bit128, lambda: grid.set_grid(128, 128))
clickListener.addListener(bit8, lambda: grid.set_grid(8, 8))
clickListener.addListener(transparent, lambda: brush.setTransparent(True))
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

    checkColor()
    clickListener.listenEvents()
    pygame.display.flip()
    CLOCK.tick(FPS)
