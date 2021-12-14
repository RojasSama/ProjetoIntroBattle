import pygame as pg
from pygame.constants import K_RIGHT, KEYDOWN, KEYUP
from character import *

class Menu():
    def __init__(self, game):
        pg.init()
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W // 2, self.game.DISPLAY_H // 2  # definindo o meio de cada eixo
        self.run_display = True
        self.cursor_img = pg.transform.scale(pg.image.load('UI/introcomp_seta(resized).png'), (18, 18))
        self.cursor_rect = pg.Rect(0, 0, 40, 40)  # armazenando as coordenadas do retangulo do cursor
        self.offset = - 100  # deslocamento do cursor
    
    def draw_cursor(self):
        self.game.draw_text('>', 25, self.cursor_rect.x, self.cursor_rect.y, self.game.WHITE)

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
            self.game.draw_text('Main Menu', 35, self.game.DISPLAY_W // 2, self.game.DISPLAY_H // 2 - 20, self.game.WHITE)
            self.game.draw_text('Start', 35, self.startx, self.starty, self.game.WHITE)
            self.game.draw_text('Credits', 35, self.creditsx, self.creditsy, self.game.WHITE)
            self.game.draw_text('Exit', 35, self.exitx, self.exity, self.game.WHITE)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.RIGHT_KEY:
            if self.state == 'Start':  # caso o cursor esteja no estado 'start', e for pressionada, a tecla 'down' 
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
                self.game.curr_menu = self.game.credits.display_menu()

            elif self.state == 'Exit':
                self.game.running, self.game.playing = False, False

            self.run_display = False

class SelectMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.position = 'priest'  # posicao inicial do cursor na tela de selecao
        self.bg = pg.transform.scale(pg.image.load('Background/cenario(menu).png'), (1024, 768))
        self.choosing, self.running = False, False
        self.team = []
        self.char = Character()
        self.state = {  # coordenadas de cada personagem no menu de selecao
            'priest': [245, 130], 'paladin': [465, 130], 'hunter': [685, 130],
            'wizard': [335, 475], 'rogue': [565, 475],
        }
    
    def draw_cursor(self, position):
        self.imgx, self.imgy = self.state[position][0] + 50, self.state[position][1] - 50  # as coordenadas do cursor sao baseadas nas dos personagens
        self.curr_img = pg.transform.scale(pg.image.load('UI/introcomp_seta(resized).png'), (35, 35))  # imagem do cursor
        img_rect = self.curr_img.get_rect()
        img_rect.center = (self.imgx, self.imgy)  # coordenadas do cursor
        self.game.display.blit(self.curr_img, img_rect)
    
    def move_cursor(self):
        if self.game.RIGHT_KEY:  # caso o jogador pressione a tecla 'seta para direita' verifique a posicao do cursor
            if self.position == 'priest':  # o cursor recebe uma nova posicao a cada movimentacao do cursor
                self.position = 'paladin'
                self.draw_cursor(self.position)  # metodo desenhar cursor

            elif self.position == 'paladin':
                self.position = 'hunter'
                self.draw_cursor(self.position)

            elif self.position == 'hunter':
                self.position = 'wizard'
                self.draw_cursor(self.position)

            elif self.position == 'wizard':
                self.position = 'rogue'
                self.draw_cursor(self.position)
            
            elif self.position == 'rogue':
                self.position = 'priest'
                self.draw_cursor(self.position)

        elif self.game.LEFT_KEY:
            if self.position == 'priest':
                self.position = 'rogue'
                self.draw_cursor(self.position)

            elif self.position == 'rogue':
                self.position = 'wizard'
                self.draw_cursor(self.position)
            
            elif self.position == 'wizard':
                self.position = 'hunter'
                self.draw_cursor(self.position)
            
            elif self.position == 'hunter':
                self.position = 'paladin'
                self.draw_cursor(self.position)
            
            elif self.position == 'paladin':
                self.position = 'priest'
                self.draw_cursor(self.position)

    def display_menu(self):
        self.run_display = True
        if self.run_display:
            self.check_input()
            self.game.display.fill(self.game.BLACK)

            self.game.display.blit(self.bg, (0,0))
            self.game.draw_text('Select your characters', 50, self.game.DISPLAY_W // 2, self.game.DISPLAY_H // 2 - 20, self.game.WHITE)

            ######## displaying ui for the characters #########
            self.game.display.blit(self.char.ui_bg, (210, 105))
            self.game.display.blit(self.char.ui_bg, (430, 105))
            self.game.display.blit(self.char.ui_bg, (650, 105))
            self.game.display.blit(self.char.ui_bg, (310, 450))
            self.game.display.blit(self.char.ui_bg, (535, 450))

            ########################################## displaying the characters ########################################################
            self.char.blit_character(self.state['priest'][0], self.state['priest'][1], self.char.catalog['priest'], self.game.display)
            self.char.blit_character(self.state['paladin'][0], self.state['paladin'][1], self.char.catalog['paladin'], self.game.display)
            self.char.blit_character(self.state['hunter'][0], self.state['hunter'][1], self.char.catalog['hunter'], self.game.display)
            self.char.blit_character(self.state['wizard'][0], self.state['wizard'][1], self.char.catalog['wizard'], self.game.display)
            self.char.blit_character(self.state['rogue'][0], self.state['rogue'][1], self.char.catalog['rogue'], self.game.display)

            self.game.draw_text('Priest', 20, 275, 230, self.game.BLACK)
            self.game.draw_text('Paladin', 20, 510, 230, self.game.BLACK)
            self.game.draw_text('Hunter', 20, 725, 230, self.game.BLACK)
            self.game.draw_text('Wizard', 20, 385, 575, self.game.BLACK)
            self.game.draw_text('Rogue', 20, 605, 575, self.game.BLACK)

            self.draw_cursor(self.position)
            self.game.reset_keys()
            self.blit_screen()

    def check_input(self):
        self.move_cursor()
        if self.game.z_KEY:
            if self.position == 'priest':
                self.select_team(Priest)
            
            elif self.position == 'paladin':
                self.select_team(Paladin)

            elif self.position == 'hunter':
                self.select_team(Hunter)

            elif self.position == 'wizard':
                self.select_team(Witch)

            elif self.position == 'rogue':
                self.select_team(Rogue)

        elif self.game.x_KEY:
            self.choosing, self.running = False, False
            self.team = []
    
    def select_team(self, character: object):
        self.choosing = True
        if not (character in self.team):
            while (self.choosing) and (len(self.team) < 3):  # enquanto o jogador estiver escolhendo o time e a lista de personagens for menor que 3
                self.team.append(character)
                print(self.team)

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.x, self.y = self.game.DISPLAY_W // 2, 10
        self.credits = ['--- Creditos ---', 
                        'Artes:',
                        'Augusto Moraes Alves',
                        'Bernardo Seibert',
                        'Geisson Venancio do Nascimento',
                        'Giulia Guimaraes',
                        'Kaique Taylor Gripa dos Santos',
                        'Kiara Pezzin Silva',
                        'Raquel Paulo Silva',
                        'Rhuan dos Santos',
                        '',
                        'Desenvolvimento do jogo:',
                        'Luiz Rojas',
                        'Andrei',
                        'Joao Paulo'
                        'Octavio Sales',
                        'Karla Sancio',
                        'Joao Gabriel de Barros Rocha',
                        '',
                        'Documentacao:',
                        'Victor Aguiar Marques']

    def display_menu(self):
        self.run_display = True

        self.lines = []
        for line in self.credits:
            self.lines.append((line, self.y))
            self.y += 25

        while self.run_display:
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            
            for content in self.lines:
                self.game.draw_text(content[0], 20, self.x, content[1], self.game.WHITE)

            self.game.reset_keys()
            self.blit_screen()

    def check_input(self):
        self.game.check_events()
        if self.game.x_KEY:
            self.run_display = False
