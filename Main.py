# imports
import keyboard as kb
import time
import random
import pygame as pg

pg.init()


# variables

sw = 960  # screen width
sh = 540  # screen height
PINK = (255, 120, 220)

# functions

def draw(n):
    pass

# main
screen = pg.display.set_mode([sw, sh])  # first is x. Second - y.
running = True
while running:
    circlex = 0
    circley = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN and event.pos == (circlex, circley):
            pass
    screen.fill((0, 0, 0))

    objcounter = 0
    for i in range(objcounter):
        draw(i)
    pg.draw.circle(screen, PINK, (random.randint(50, sw - 50), random.randint(50, sh - 50)), 50)

    pg.display.flip()

pg.quit()
