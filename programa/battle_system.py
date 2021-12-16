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
        # self.Character
        self.turn = 'Player'
        self.position = 'Attack'
        self.coord_enemies = {'witch': [850, 75], 'skeleton': [850, 450]}

    def show_hp(self):
        # total_hp_team = [self.player_team[0].health, self.player_team[1].health, self.player_team[2].health]
        # current_hp = total_hp_team.copy()
        
        self.game.draw_text(f'{Rogue.__name__} - {12} / {100}', 35, 850, 550, self.game.BLACK)
        self.game.draw_text(f'{Wizard.__name__} - {50} / {100}', 35, 850, 600, self.game.BLACK)
        self.game.draw_text(f'{Hunter.__name__} - {75} / {100}', 35, 850, 650, self.game.BLACK)
    
    def display_scenery(self):
        
        self.running = True
        if self.running:

            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.bg_img, (0, 0))
            self.game.display.blit(self.ui_1, (5, 510))
            self.game.display.blit(self.ui_2, (660, 510))

            if self.turn == 'Player':
                self.game.draw_text("Player's turn!", 40, 175, 560, self.game.BLACK)
                self.game.draw_text('Attack', 35, 175, 650, self.game.BLACK)
                self.game.draw_text('Defensor', 35, 390, 650, self.game.BLACK)

                self.show_hp()

            ########################################### Apresentando problemas ################################################################################
            # self.player_team[0].blit_character(250, 75, self.player_team[0].img, self.game.display)
            # self.player_team[1].blit_character(50, 250, self.player_team[1].img, self.game.display)
            # self.player_team[2].blit_character(250, 450, self.player_team[3].img, self.game.display)

            Character.blit_character(self.coord_enemies['witch'][0], self.coord_enemies['witch'][1], 75, self.game.char.catalog['witch'], self.game.display)
            # Character.blit_character(self.coord_enemies['Skeleton'][0], self.coord_enemies['Skeleton'][1], Character.catalog['skeleton'], self.game.display)
            ####################################################################################################################################################

            self.game.main_menu.blit_screen()
    
    def draw_cursor(self):
        pass

class Turn(Battle):
    def __init__(self):
        super().__init__(self)
        self.playing = self.player_team[0]
    
    def hero_turn(self):
        self.speed_heroes = [x for x in self.game.selection.team.speed]
