import pygame as pg
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
                self.game.selection.running = True
            
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits.display_menu()

            elif self.state == 'Exit':
                self.game.running, self.game.playing = False, False

            self.run_display = False

class SelectMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.position = 'Priest'  # posicao inicial do cursor na tela de selecao
        self.bg = pg.transform.scale(pg.image.load('Background/cenario(menu).png'), (1024, 768))
        self.choosing, self.running = False, False
        self.char = Character()
        self.state = {  # coordenadas de cada personagem no menu de selecao
            'Priest': [245, 130], 'Paladin': [465, 130], 'Hunter': [685, 130],
            'Wizard': [335, 475], 'Rogue': [565, 475],
        }
    
    def draw_cursor(self, position):
        self.imgx, self.imgy = self.state[position][0] + 50, self.state[position][1] - 50  # as coordenadas do cursor sao baseadas nas dos personagens
        self.curr_img = pg.transform.scale(pg.image.load('UI/introcomp_seta(resized).png'), (35, 35))  # imagem do cursor
        img_rect = self.curr_img.get_rect()
        img_rect.center = (self.imgx, self.imgy)  # coordenadas do cursor
        self.game.display.blit(self.curr_img, img_rect)
    
    def move_cursor(self):
        if self.game.RIGHT_KEY:  # caso o jogador pressione a tecla 'seta para direita' verifique a posicao do cursor
            if self.position == 'Priest':  # o cursor recebe uma nova posicao a cada movimentacao do cursor
                self.position = 'Paladin'
                self.draw_cursor(self.position)  # metodo desenhar cursor

            elif self.position == 'Paladin':
                self.position = 'Hunter'
                self.draw_cursor(self.position)

            elif self.position == 'Hunter':
                self.position = 'Wizard'
                self.draw_cursor(self.position)

            elif self.position == 'Wizard':
                self.position = 'Rogue'
                self.draw_cursor(self.position)
            
            elif self.position == 'Rogue':
                self.position = 'Priest'
                self.draw_cursor(self.position)

        elif self.game.LEFT_KEY:
            if self.position == 'Priest':
                self.position = 'Rogue'
                self.draw_cursor(self.position)

            elif self.position == 'Rogue':
                self.position = 'Wizard'
                self.draw_cursor(self.position)
            
            elif self.position == 'Wizard':
                self.position = 'Hunter'
                self.draw_cursor(self.position)
            
            elif self.position == 'Hunter':
                self.position = 'Paladin'
                self.draw_cursor(self.position)
            
            elif self.position == 'Paladin':
                self.position = 'Priest'
                self.draw_cursor(self.position)

    def display_menu(self):
        if not self.game.battle_system.running:
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
            self.char.blit_character(self.state['Priest'][0], self.state['Priest'][1], self.char.catalog['Priest'], self.game.display)
            self.char.blit_character(self.state['Paladin'][0], self.state['Paladin'][1], self.char.catalog['Paladin'], self.game.display)
            self.char.blit_character(self.state['Hunter'][0], self.state['Hunter'][1], self.char.catalog['Hunter'], self.game.display)
            self.char.blit_character(self.state['Wizard'][0], self.state['Wizard'][1], self.char.catalog['Wizard'], self.game.display)
            self.char.blit_character(self.state['Rogue'][0], self.state['Rogue'][1], self.char.catalog['Rogue'], self.game.display)

            ################# displaying the texts ######################
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
            if self.position == 'Priest':
                self.select_team(Priest())
            
            elif self.position == 'Paladin':
                self.select_team(Paladin())

            elif self.position == 'Hunter':
                self.select_team(Hunter())

            elif self.position == 'Wizard':
                self.select_team(Wizard())

            elif self.position == 'Rogue':
                self.select_team(Rogue())

        elif self.game.x_KEY:
            self.choosing, self.running, self.run_display = False, False, False
                    
        elif len(crew) == 3:
            self.running, self.choosing, self.run_display = False, False, False
            self.game.battle_system.running = True
    
    def select_team(self, character):
        self.choosing = True
        if not (character in crew):
            if (self.choosing) and (len(crew) < 3):  # se o jogador estiver escolhendo o time, e o tamanho da lista time for menor que 3
                crew.append(character)

crew = []

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.x, self.y = self.game.DISPLAY_W // 2, 10
        self.credits = ['--- Creditos ---',
                        '',
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
                        'Joao Paulo',
                        'Octavio Sales',
                        'Karla Sancio',
                        'Joao Gabriel de Barros Rocha',
                        '',
                        'Documentacao:',
                        'Victor Aguiar Marques']

    def display_menu(self):
        self.run_display = True

        self.y = 65
        self.lines = []
        for line in self.credits:
            self.lines.append((line, self.y))
            self.y += 25

        while self.run_display:
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            
            for content in self.lines:
                self.game.draw_text(content[0], 35, self.x, content[1], self.game.WHITE)

            self.game.reset_keys()
            self.blit_screen()

    def check_input(self):
        self.game.check_events()
        if self.game.x_KEY:
            self.run_display = False
