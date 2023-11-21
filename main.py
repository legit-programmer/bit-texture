import pygame
import random

pygame.init()

WIDTH, HEIGHT = (1280, 720)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()

running = True
WIN.fill((255, 255, 255))


class Particle:
    def __init__(self, radius: int, color: tuple) -> None:
        self.r = radius
        self.x = self.r
        self.y = random.randrange(self.r, HEIGHT-self.r)
        self.color = color
        self.ux = 1
        self.uy = 0
        self.vel = random.randrange(0, 50)

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.vel*self.ux
        self.y += self.vel*self.uy

    def determine(self):
        bowl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        choice = random.choice(bowl)
        if choice == 9:
            self.uy = ((random.randrange(0, 9)/10)) * random.choice([-1, 1])


particles = list()


def generateParticles(number: int):
    for _ in range(number):
        R = random.randrange(0, 255)
        G = random.randrange(0, 255)
        B = random.randrange(0, 255)

        particles.append(Particle(1, (R, G, B)))


def drawParticles():
    for particle in particles:
        particle.draw()
        particle.determine()
        particle.move()


generateParticles(1000)
while running:
    # WIN.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    drawParticles()
    pygame.display.flip()
    CLOCK.tick(FPS)
