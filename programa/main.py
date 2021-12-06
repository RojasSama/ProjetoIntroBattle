# -*- coding: UTF-8 -*-

import pygame as pg
from pygame.locals import *
import sys

pg.init()  # iniciando os modulos da biblioteca
pg.font.init()

def draw_text(text, font, type, color, surface, x, y):  # funcao que desenha um texto na tela a partir de alguns parametros
    textObj = font.render(text, type, color)  # rendenizando a fonte
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)  # definindo a posicao do texto na tela
    surface.blit(textObj, textRect)  # desenhando o texto escolhido
    
def menu():
    draw_text('Main Menu', font, 1, (255, 255, 255), screen, 40, 30)
    draw_text('Press "Z" to play', font, 2, (120, 255, 120), screen, 40, 125)
    draw_text('Press "escape" to exit', font, 2, (235, 25, 25), screen, 40, 160)

screen_size = (1024, 768)  # resolucao da tela
screen = pg.display.set_mode((screen_size[0], screen_size[1]))
pg.display.set_caption('Intro Battle')  # titulo da janela

font = pg.font.SysFont(None, 50)  # declarando a fonte do sistema para ser usada

clock = pg.time.Clock()

# bg_music = pg.mixer.music.load('musicas/BoxCat Games - Defeat.mp3')  # declarando a musica de fundo
# pg.mixer.music.set_volume(0.35)  # definindo o volume da musica de fundo
# pg.mixer.music.play(-1)  # fazendo com que a musica fique em loop


running = True
while running:  # loop principal

    screen.fill([0, 0, 0])
    
    menu1 = menu()
    
    clock.tick(30)  # taxa de quadros
    pg.display.flip()  # a tela sera atualizada a cada iteracao do loop

    for event in pg.event.get():  # tratamento de eventos
        if event.type == QUIT:
            pg.quit()
            sys.exit()
