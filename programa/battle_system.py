import pygame as pg
from menu import *
from game import *

class Battle():
    def __init__(self, game):
        self.game = game
        self.bg_img = pg.transform.scale(pg.image.load('Background/cenario(lutas).png'), (1024, 768))
        self.ui_1 = pg.transform.scale(pg.image.load('UI/introcomp_menu(resized).png'), (650, 285))
        self.ui_2 = pg.transform.scale(self.ui_1, (360, 285))
        self.cursor = pg.transform.scale(pg.image.load('UI/introcomp_seta(resized).png'), (10, 10))


    def display_scenery(self):
        self.game.display.fill(self.game.BLACK)
        self.game.display.blit(self.bg_img, (0, 0))
        self.game.display.blit(self.ui_1, (5, 475))
        self.game.display.blit(self.ui_2, (660, 475))
        Menu.blit_screen(self)
