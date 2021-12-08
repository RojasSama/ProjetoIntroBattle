import pygame
from pygame.locals import *
from menu import MainMenu


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False  
        self.z_KEY, self.x_KEY, self.RIGHT_KEY, self.LEFT_KEY = False, False, False, False  # definindo o valor 'default' das teclas que serao usadas
        self.DISPLAY_W, self.DISPLAY_H = 1024, 768  # dimensoes da tela 
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        pygame.display.set_caption('Intro Battle')  # definindo nome da janela
        self.font_name = 'programa/FreePixel.ttf'  # fonte do jogo
        # self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.crr_menu = MainMenu(self)

    def game_loop(self):  # loop principal
        clock = pygame.time.Clock()
        while self.playing:
            clock.tick(30)  # definindo a taxa de quadros
            self.check_events()
            if self.z_KEY:
                self.playing = False
            self.display.fill(self.BLACK)  # preenchendo a tela com a cor preta
            self.draw_text('Select your characters', 45, self.DISPLAY_W // 2, self.DISPLAY_H // 2)  # desenhando na tela usando os parametros largura e altura da tela
            self.window.blit(self.display, (0, 0))  # 'blitando' o display na janela 'window'
            pygame.display.flip()  # atualiza o display a cada iteracao do loop
            self.reset_keys()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.crr_menu.run_display = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.z_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.x_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
    
    def reset_keys(self):
        self.z_KEY, self.x_KEY, self.RIGHT_KEY, self.LEFT_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
        