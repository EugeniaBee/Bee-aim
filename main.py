# imports
# import keyboard as kb
import time
import random
import pygame as pg

pg.init()


# variables

sw = 1280  # screen width
sh = 720  # screen height

PINK = (255, 120, 220)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ez_font = pg.font.SysFont('Comic Sans MS', 15)


# functions

def draw(n):
    pass


# main

screen = pg.display.set_mode([sw, sh])  # first is x. Second - y.

running = True

cc = 0
pc = 0
radius = 60
circlex = random.randint(100, sw - 50)
circley = random.randint(80, sh - 50)

while running:
    screen.fill((0, 0, 0))

    if cc != 0 or pc != 0:
        radius = 60 * (1.4 - round(cc/(cc+pc), 3))
    else:
        radius = 60

    objcounter = 0
    for i in range(objcounter):
        draw(i)

    pg.draw.circle(screen, BLUE, (circlex, circley), radius)

    pg.display.set_caption('AimBee')

    information_line1 = 'Circles popped ' + str(cc)
    information_line2 = 'Shots missed ' + str(pc)
    information_line3 = 'Shots made ' + str(cc + pc)
    if cc != 0 or pc != 0:
        information_line4 = 'Percentage ' + str(round(cc/(cc+pc)*100, 3)) + '%'
    else:
        information_line4 = 'Percentage ' + '-' + '%'

    text_surface1 = ez_font.render(information_line1, True, WHITE)
    text_surface2 = ez_font.render(information_line2, True, WHITE)
    text_surface3 = ez_font.render(information_line3, True, WHITE)
    text_surface4 = ez_font.render(information_line4, True, WHITE)

    screen.blit(text_surface1, (10, 10))
    screen.blit(text_surface2, (10, 30))
    screen.blit(text_surface3, (10, 50))
    screen.blit(text_surface4, (1140, 10))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN and ((circlex-radius < event.pos[0] < circlex+radius) and (circley-radius < event.pos[1] < circley+radius)):
            print(event.pos)
            circlex = random.randint(100, sw - 50)
            circley = random.randint(80, sh - 50)
            cc += 1
            print(cc)
        elif event.type == pg.MOUSEBUTTONDOWN:
            pc += 1

    pg.display.flip()

pg.quit()
