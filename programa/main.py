# -*- coding: UTF-8 -*-

import pygame as pg
from pygame.locals import *
import sys

pg.init()
pg.font.init()

bg_music = pg.mixer.music.load('musicas/BoxCat Games - Defeat.mp3')
pg.mixer.music.play(-1)

screen_size = (1024, 768)
screen = pg.display.set_mode((screen_size[0], screen_size[1]))
pg.display.set_caption('Intro Battle')

font = pg.font.SysFont(None, 50)

clock = pg.time.Clock()

def draw_text(text, font, type, color, surface, x, y):
    textObj = font.render(text, type, color)
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObj, textRect)
    
class MainMenu:
    def __init__(self):
        running = True
        while running:
                
            screen.fill([0, 0, 0])
            draw_text('Main Menu', font, 1, (255, 255, 255), screen, 40, 30)
            
            clock.tick(30)
            pg.display.update()
            
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

    # @classmethod
    # def draw_text(self, text, font, type, color, surface, x, y):
    #     textObj = font.render(text, type, color)
    #     textRect = textObj.get_rect()
    #     textRect.topleft = (x, y)
    #     surface.blit(textObj, textRect)
            
# def main_menu():
#     running = True
#     while running:

#         screen.fill([0, 0, 0])
#         draw_text('Main Menu', font, 1, (255, 255, 255), screen, 40, 30)
        
#         clock.tick(30)
#         pg.display.update()
        
#         for event in pg.event.get():
#             if event.type == QUIT:
#                 pg.quit()
#                 sys.exit()

menu1 = MainMenu()
menu1.draw_text('Main Menu', font, 1, (255, 255, 255), screen, 40, 30)
