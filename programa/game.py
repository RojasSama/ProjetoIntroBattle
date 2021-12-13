import pygame as pg
from pygame.locals import *
from menu import *
from battle_system import Battle


class Game():
    def __init__(self):
        pg.init()
        self.running, self.playing = True, False  

        self.z_KEY, self.x_KEY, self.RIGHT_KEY, self.LEFT_KEY = False, False, False, False  # definindo o valor 'default' das teclas que serao usadas
        self.DISPLAY_W, self.DISPLAY_H = 1024, 768  # dimensoes da tela 
        self.display = pg.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pg.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))

        pg.display.set_caption('Intro Battle')  # definindo nome da janela
        self.font_name = 'programa/FreePixel.ttf'  # fonte do jogo

        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        self.battle_system = Battle(self)
        self.selection = SelectMenu(self)
        self.main_menu = MainMenu(self)
        self.credits = CreditsMenu(self)
        self.crr_menu = self.main_menu  # menu inicial sendo o principal

    def game_loop(self):  # loop principal
        clock = pg.time.Clock()
        while self.playing:

            clock.tick(30)  # definindo a taxa de quadros por segundo
            self.check_events()

            if self.x_KEY:
                self.playing = False

            self.display.fill(self.BLACK)  # preenchendo a tela com a cor preta
            self.window.blit(self.display, (0, 0))  # 'blitando' o display na janela 'window'
            # self.battle_system.display_scenery()
            self.selection.display_menu()  # exibindo o menu de selecao

            pg.display.flip()  # atualiza o display a cada iteracao do loop
            self.reset_keys()  # reinicia as teclas para o valor padrao

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running, self.playing = False, False
                self.crr_menu.run_display = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    self.z_KEY = True
                if event.key == pg.K_x:
                    self.x_KEY = True
                if event.key == pg.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pg.K_LEFT:
                    self.LEFT_KEY = True

    def reset_keys(self):
        self.z_KEY, self.x_KEY, self.RIGHT_KEY, self.LEFT_KEY = False, False, False, False

    def draw_text(self, text, size, x, y, color):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
