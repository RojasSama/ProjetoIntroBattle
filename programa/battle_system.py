import pygame as pg
from game import *
from character import *

class Battle():
    def __init__(self, game):
        self.game = game
        self.running, self.playing = False, False
        self.bg_img = pg.transform.scale(pg.image.load('Background/cenario(lutas).png'), (1024, 768))
        self.ui_1 = pg.transform.scale(pg.image.load('UI/introcomp_menu(resized).png'), (650, 250))
        self.ui_2 = pg.transform.scale(self.ui_1, (360, 250))
        self.cursor = pg.transform.scale(pg.image.load('UI/introcomp_seta(resized).png'), (10, 10))
        self.player_team = [Rogue, Wizard, Hunter]
        self.coord_enemies = {'Witch': [850, 75], 'Skeleton': [850, 450]}


    def display_scenery(self):
        
        self.running = True
        if self.running:

            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.bg_img, (0, 0))
            self.game.display.blit(self.ui_1, (5, 510))
            self.game.display.blit(self.ui_2, (660, 510))
            

            ########################################### Apresentando problemas ################################################################################
            self.player_team[0].blit_character(250, 75, self.player_team[0].img, self.game.display)
            self.player_team[1].blit_character(50, 250, self.player_team[1].img, self.game.display)
            self.player_team[2].blit_character(250, 450, self.player_team[3].img, self.game.display)

            Character.blit_character(self.coord_enemies['witch'][0], self.coord_enemies['witch'][1], 75, Character.catalog['witch'], self.game.display)
            Character.blit_character(self.coord_enemies['Skeleton'][0], self.coord_enemies['Skeleton'][1], Character.catalog['Skeleton'], self.game.display)
            ####################################################################################################################################################

            self.game.main_menu.blit_screen()
