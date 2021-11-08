import pygame as pg
from pygame.locals import *

pg.init()

dimGray = (105, 105, 105)

display_surface = pg.display.set_mode((1024, 768))

pg.display.set_caption('Intro Battle!')

bg = pg.image.load('Background\cenario(lutas).png')
cacadora = pg.transform.scale2x(pg.transform.scale2x(pg.image.load('Personagens\cacadora.png')))

'''def menu(chave, indice):
    interface = {
        'tela menu': [pg.transform.scale2x(pg.image.load('UI\introcomp_menu.png')), (960, 700)]
    }
    return interface[chave][indice]'''

relogio = pg.time.Clock()
pos_cacadora = [512, 384]

rodando = True
while rodando:

    relogio.tick(30)
    
    display_surface.fill(dimGray)
    display_surface.blit(bg, (0, 0))
    display_surface.blit(cacadora, (pos_cacadora[0], pos_cacadora[1]))
    # display_surface.blit(menu('tela menu', 0), menu('tela menu', 1))
    
    for event in pg.event.get():

        if event.type == pg.QUIT:
            rodando = False
        
        # if event.type == pg.KEYDOWN:

            # if event.key == pg.K_UP:
            #     pos_cacadora[1] -= 5
            # if event.key == pg.K_DOWN:
            #     pos_cacadora[1] += 5   
            # if event.key == pg.K_LEFT:
            #     pos_cacadora[0] -= 5
            # if event.key == pg.K_RIGHT:
            #     pos_cacadora[0] += 5

    if pg.key.get_pressed()[K_w]:
        pos_cacadora[1] -= 15
    if pg.key.get_pressed()[K_s]:
        pos_cacadora[1] += 15   
    if pg.key.get_pressed()[K_a]:
        pos_cacadora[0] -= 15   
    if pg.key.get_pressed()[K_d]:   
        pos_cacadora[0] += 15 
    if pg.key.get_pressed()[K_ESCAPE]:
        rodando = False
    pg.display.update()
