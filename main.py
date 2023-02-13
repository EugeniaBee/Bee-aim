# imports
# import keyboard as kb
# import time
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
c = 0
while running:
    circlex = random.randint(50, sw - 50)
    circley = random.randint(50, sh - 50)

    screen.fill((0, 0, 0))

    objcounter = 0
    for i in range(objcounter):
        draw(i)
    pg.draw.circle(screen, PINK, (circlex, circley), 50)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN and event.pos == (circlex, circley):
            c += 1
            print(c)

    pg.display.flip()

pg.quit()
