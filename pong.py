import pygame as pg
from random import randint, random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

pg.init()
clock = pg.time.Clock()
sc = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Pong222')

# BG_COLOR = pygame.Color('grey12')
BG_COLOR = (80, 50, 50)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    x = ((randint(0, 255), randint(4, 100), randint(3, 100)))
    print(random())
    sc.fill(x)

    clock.tick(25)
    pg.display.flip()
