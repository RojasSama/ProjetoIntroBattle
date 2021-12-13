import pygame as pg
from menu import *

class Battle():
    def __init__(self):
        self.bg_img = pg.transform.scale(pg.image.load('Background/cenario(lutas).png'), (1024, 768))
        pass

    def display_scenery(self):
        self.game.display.blit(self.bg_img, (0, 0))
        pass
