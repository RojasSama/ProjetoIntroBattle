import pygame 

class Menu():
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W // 2, self.game.DISPLAY_H // 2  # definindo o meio de cada eixo
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 40, 40)  # armazenando as coordenadas do retangulo do cursor
        self.offset = - 100  # deslocamento do cursor
    
    def draw_cursor(self):
        self.game.draw_text('#', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))  # instanciando o obj game para blitar na tela o display nas coordenadas (0, 0)
        pygame.display.flip()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'  # onde o cursor inicia no menu principal
        self.startx, self.starty = self.mid_w, self.mid_h + 30  # definindo eixos do start e afins
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
        if self.game.RIGTH_KEY:
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
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            
            elif self.state == 'Credits':
                pass
            elif self.state == 'Exit':
                pass
            self.run_display = False 