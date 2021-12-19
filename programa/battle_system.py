import pygame as pg
from game import *
from character import *

class Battle(SelectMenu):
    def __init__(self, game):
        SelectMenu.__init__(self, game)
        self.game = game
        self.running, self.playing = False, False
        self.bg_img = pg.transform.scale(pg.image.load('Background/cenario(lutas).png'), (1024, 768))
        self.ui_1 = pg.transform.scale(pg.image.load('UI/introcomp_menu(resized).png'), (650, 250))
        self.ui_2 = pg.transform.scale(self.ui_1, (360, 250))
        self.cursor = pg.transform.scale(pg.image.load('UI/introcomp_seta(resized).png'), (25, 25))
        self.turn = 'player'
        self.position = 'attack'
        self.coord_enemies = {'witch': [850, 185, pg.transform.flip(SelectMenu(self.game).char.catalog['witch'], True, False)], 'skeleton': [850, 350, pg.transform.flip(SelectMenu(self.game).char.catalog['skeleton'], True, False)]}
    
    def display_cursor(self, position):
        self.positions = {'attack' : [45, 700], 'defend' : [260, 700]}
        
        self.imgx, self.imgy = self.positions[position][0] + 50, self.positions[position][1] - 50  # as coordenadas do cursor sao baseadas nas dos personagens
        img_rect = self.cursor.get_rect()
        img_rect.center = (self.imgx, self.imgy)  # coordenadas do cursor
        self.game.display.blit(pg.transform.rotate(self.cursor, 90), img_rect)
    
    def move_cursor(self):
        if self.game.RIGHT_KEY:
            if self.position == 'attack':
                self.position = 'defend'
                self.display_cursor(self.position)
        
        elif self.game.LEFT_KEY:
            if self.position == 'defend':
                self.position = 'attack'
                self.display_cursor(self.position)

    def show_hp(self):
        self.game.draw_text(f'{Rogue.__class__.__name__} - {12} / {100}', 35, 850, 550, self.game.BLACK)
        self.game.draw_text(f'{Wizard.__class__.__name__} - {50} / {100}', 35, 850, 600, self.game.BLACK)
        self.game.draw_text(f'{Hunter.__class__.__name__} - {75} / {100}', 35, 850, 650, self.game.BLACK)

    def display_scenery(self):
        
        self.running = True
        if self.running:
            self.game.check_events()

            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.bg_img, (0, 0))
            self.game.display.blit(self.ui_1, (5, 510))
            self.game.display.blit(self.ui_2, (660, 510))

            if self.turn == 'player':
                self.game.draw_text("Player's turn!", 40, 175, 560, self.game.BLACK)
                self.game.draw_text('Attack', 35, 175, 650, self.game.BLACK)
                self.game.draw_text('Defend', 35, 390, 650, self.game.BLACK)

                self.show_hp()

                Character().blit_character(50, 185, SelectMenu(self.game).char.catalog['rogue'], self.game.display)
                Character().blit_character(90, 255, SelectMenu(self.game).char.catalog['wizard'], self.game.display)
                Character().blit_character(50, 350, SelectMenu(self.game).char.catalog['hunter'], self.game.display)

            self.move_cursor()
            ########################################### Apresentando problemas #######################
            # self.player_team[0].blit_character(250, 75, self.player_team[0].img, self.game.display)
            # self.player_team[1].blit_character(50, 250, self.player_team[1].img, self.game.display)
            # self.player_team[2].blit_character(250, 450, self.player_team[3].img, self.game.display)
            ##########################################################################################
            
            Character().blit_character(self.coord_enemies['witch'][0], self.coord_enemies['witch'][1], self.coord_enemies['witch'][2], self.game.display)
            Character().blit_character(self.coord_enemies['skeleton'][0], self.coord_enemies['skeleton'][1], self.coord_enemies['skeleton'][2], self.game.display)

            self.game.main_menu.blit_screen()
            # self.game.reset_keys()

class Turn(Battle):
    def __init__(self):
        super().__init__(self)
        self.playing = self.player_team[0]
    
    def hero_turn(self):
        self.speed_heroes = [x for x in self.game.selection.team.speed]
