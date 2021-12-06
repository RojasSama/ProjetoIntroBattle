# -*- coding: UTF-8 -*-

import pygame as pg
from pygame.locals import *
import sys

from classes import Character

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
    draw_text('Press "escape" to exit', font, 2, (235, 25, 25), screen, 40, 160)  # possivel adicao

def choice_menu():
    characters = {'mago': 0, 'bruxa': 1, 'vampiro': 2, 'caveira': 3, 'clerigo': 4, 'paladino': 5, 'cacadora': 6}

    arrow = pg.image.load('UI/introcomp_seta.png')
    arrow_xy = 50, 90
    bg = pg.image.load('Background/cenario(lutas).png')
    ui_bg = pg.image.load('UI/introcomp_menu.png')

    count = 1
    running = True
    while running:

        screen.blit(Character.catalog['mago'], (50, 75))
        screen.blit(Character.catalog['bruxa'], (150, 75))
        screen.blit(Character.catalog['vampiro'], (250, 75))
        screen.blit(Character.catalog['caveira'], (350, 75))
        screen.blit(Character.catalog['clerigo'], (75, 105))
        screen.blit(Character.catalog['paladino'], (175, 105))
        screen.blit(Character.catalog['cacadora'], (275, 105))

        for event in pg.event.get():
            if event.type == QUIT:
                running = False
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN:
                
                if event.key == K_RIGHT:
                    count += 1
        
        for n in characters.values():
            if n == count and n <= 4:
                screen.blit(arrow, (arrow_xy[0], arrow_xy[1]))
                
        screen.blit(bg, (0, 0))
        screen.blit(ui_bg, (20, 50))
    

screen_size = x, y = (1024, 768)  # resolucao da tela
screen = pg.display.set_mode((screen_size[0], screen_size[1]))
pg.display.set_caption('Intro Battle')  # titulo da janela

font = pg.font.SysFont(None, 50)  # declarando a fonte do sistema para ser usada

clock = pg.time.Clock()

bg_music = pm.mixer.music.load('musicas/BoxCat Games - Defeat.mp3')  # declarando a musica de fundo
pm.mixer.music.set_volume(0.35)  # definindo o volume da musica de fundo
pm.mixer.music.play(-1)  # fazendo com que a musica fique em loop


choice_char = False
running = True
while running:  # loop principal

    screen.fill([0, 0, 0])
    menu()

    for event in pg.event.get():  # tratamento de eventos
        if event.type == QUIT:
            running = False
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_z:
                choice_char = True
                choice_menu()

            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit()

    clock.tick(30)  # taxa de quadros
    pg.display.flip()  # a tela sera atualizada a cada iteracao do loop