# -*- coding: UTF-8 -*-

import pygame as pg
from pygame.locals import *

pg.init()
pg.font.init()

def main_menu(surface):
    font = pg.font.SysFont('arial', 120, False, False)
    message = 'Intro Battle!'
    text_formatted = font.render(message, True, (205, 55, 0))
    surface.blit(text_formatted, (512, 384))
    
def main():
    height, width = 1024, 768
    display_surface = pg.display.set_mode((height, width))
    pg.display.set_caption('Intro Battle!')

    ##########################

    font = pg.font.SysFont('arial', 120, False)
    message = 'Intro Battle!'
    text_formatted = font.render(message, True, (205, 55, 0))
     
    ##########################

    bg_color = (105, 105, 105)
    clock = pg.time.Clock()

    while True:  # main loop

        clock.tick(30)
        display_surface.fill(bg_color)
        display_surface.blit()
        main_menu(display_surface)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()

if __name__ == '__main__':
    main()
