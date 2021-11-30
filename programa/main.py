# -*- coding: UTF-8 -*-

import pygame as pg
from pygame.locals import *
import sys

pg.init()
pg.font.init()

pg.mixer.music.set_volume(0.35)  # definindo o volume da musica de fundo

def draw_text(text, font, type, color, surface, x, y):  # funcao que desenha um texto na tela a partir de alguns parametros
    textObj = font.render(text, type, color)  # rendenizando a fonte
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)  # definindo a posicao do texto na tela
    surface.blit(textObj, textRect)  # desenhando o texto escolhido
    
def menu():
    draw_text('Main Menu', font, 1, (255, 255, 255), screen, 40, 30)

screen_size = (1024, 768)  # resolucao da tela
screen = pg.display.set_mode((screen_size[0], screen_size[1]))
pg.display.set_caption('Intro Battle')  # titulo da janela

font = pg.font.SysFont(None, 50)  # declarando a fonte do sistema para ser usada

clock = pg.time.Clock()

bg_music = pg.mixer.music.load('musicas/BoxCat Games - Defeat.mp3')  # declarando a musica de fundo
pg.mixer.music.play(-1)  # fazendo com que a musica fique em loop


running = True
while running:  # loop principal

    screen.fill([0, 0, 0])
    
    menu1 = menu()
    clock.tick(30)
    pg.display.update()

    for event in pg.event.get():  # tratamento de eventos
        if event.type == QUIT:
            pg.quit()
            sys.exit()
