import pygame as pg
from character import *

class Menu():
    def __init__(self, game):
        pg.init()
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W // 2, self.game.DISPLAY_H // 2  # definindo o meio de cada eixo
        self.run_display = True
        self.cursor_img = pg.transform.scale(pg.image.load('UI/introcomp_seta(resized).png'), (200, 200))
        self.cursor_rect = pg.Rect(0, 0, 40, 40)  # armazenando as coordenadas do retangulo do cursor
        self.offset = - 100  # deslocamento do cursor
        # self.arrow = pygame.image.load('UI/introcomp_seta.png')
    
    def draw_cursor(self):
        # pygame.transform.rotate(self.arrow, - 90)
        self.game.draw_text('>', 25, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))  # instanciando o obj game para blitar na tela o display nas coordenadas (0, 0)
        pg.display.flip()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'  # onde o cursor inicia no menu principal
        self.startx, self.starty = self.mid_w, self.mid_h + 30  # definindo eixos da opcao start e afins
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 60
        self.exitx, self.exity = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 35, self.game.DISPLAY_W // 2, self.game.DISPLAY_H // 2 - 20)
            self.game.draw_text('Start', 35, self.startx, self.starty)
            self.game.draw_text('Credits', 35, self.creditsx, self.creditsy)
            self.game.draw_text('Exit', 35, self.exitx, self.exity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.RIGHT_KEY:
            if self.state == 'Start':  # caso o cursor esteja estado 'start' e for pressionada a tecla 'down' 
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)  # sera deslocado para a proxima opcao do menu
                self.state = 'Credits'  # e reajusta o estado da posicao do cursor

            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.exity)
                self.state = 'Start'

        elif self.game.LEFT_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
                
            if self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

            if self.state == 'Exit':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
    
    def check_input(self):
        self.move_cursor()
        if self.game.z_KEY:
            if self.state == 'Start':
                self.game.playing = True
            
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits

            elif self.state == 'Exit':
                self.game.running, self.game.playing = False, False

            self.run_display = False

class SelectMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.bg = pg.transform.scale(pg.image.load('Background/cenario(menu).png'), (1024, 768))
        self.char = Character()
        self.state = {  # coordenadas de cada personagem no menu de selecao
            'wizard': [12, 18], 'witch': [262, 18], 'vampire': [512, 40], 'skeleton': [762, 18],
            'cleric': [125, 108], 'paladin': [375, 108], 'hunter': [625, 108]
        }
    
    def draw_cursor(self):
        self.imgx, self.imgy = 30, 8
        img = pg.image.load('UI/introcomp_seta(resized).png')
        img_rect = img.get_rect()
        img_rect.center = (self.imgx, self.imgy)
        self.game.display.blit(self.char.arrow, img_rect)
    
    def display_menu(self):
        self.run_display = True
        if self.run_display:
            self.game.check_events()
            # self.check_input()
            self.game.display.fill(self.game.BLACK)

            self.game.display.blit(self.bg, (0,0))

            ################### displaying ui for characters ##############################
            self.char.blit_character(12, 18, self.char.ui_bg, self.game.display)
            self.char.blit_character(262, 18, self.char.ui_bg, self.game.display)
            self.char.blit_character(512, 18, self.char.ui_bg, self.game.display)
            self.char.blit_character(762, 18, self.char.ui_bg, self.game.display)
            self.char.blit_character(125, 108, self.char.ui_bg, self.game.display)
            self.char.blit_character(375, 108, self.char.ui_bg, self.game.display)
            self.char.blit_character(625, 108, self.char.ui_bg, self.game.display)

            ######################## displaying the characters ############################
            self.char.blit_character(self.state['wizard'][0], self.state['wizard'][1], self.char.catalog['wizard'], self.game.display)
            self.char.blit_character(self.state['witch'][0], self.state['witch'][1], self.char.catalog['witch'], self.game.display)
            self.char.blit_character(self.state['vampire'][0], self.state['vampire'][1], self.char.catalog['vampire'], self.game.display)
            self.char.blit_character(self.state['skeleton'][0], self.state['skeleton'][1], self.char.catalog['skeleton'], self.game.display)
            self.char.blit_character(self.state['cleric'][0], self.state['cleric'][1], self.char.catalog['cleric'], self.game.display)
            self.char.blit_character(self.state['paladin'][0], self.state['paladin'][1], self.char.catalog['paladin'], self.game.display)
            self.char.blit_character(self.state['hunter'][0], self.state['hunter'][1], self.char.catalog['hunter'], self.game.display)

            # self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.z_KEY:
            if self.state == self.state['wizard']:
                pass
        

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.credits = f'''--- Creditos ---
        Artes:
        Augusto Moraes Alves
        Bernardo Seibert
        Geisson Venancio do Nascimento
        Giulia Guimaraes
        Kaique Taylor Gripa dos Santos
        Kiara Pezzin Silva
        Raquel Paulo Silva
        Rhuan dos Santos

        Desenvolvimento do jogo:
        Luiz Rojas

        Documentacao:
        Victor Aguiar Marques'''
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.z_KEY or self.game.x_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(self.credits, 10, self.game.DISPLAY_W // 2, self.game.DISPLAY_H // 2 - 20)
            self.blit_screen()
