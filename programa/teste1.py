import pygame as pg
from pygame.locals import *

pg.init()

altura, largura = 1024, 768
TELA = pg.display.set_mode((altura, largura))  # resolução da tela

pg.display.set_caption('Intro Battle')  # titulo da janela

TELA.fill([0, 0, 0])  # cor do background (preto)

relogio = pg.time.Clock()

x = largura // 2
y = altura // 2
# meio da tela (largura / 2) - (largura_objeto / 2)

while True:  # loop pricipal do jogo

    relogio.tick(30)
    TELA.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()

    pg.draw.rect(TELA, (120, 0, 50), (x, y, 220, 175))

    if pg.key.get_pressed()[K_w]:
        y -= 15
    if pg.key.get_pressed()[K_s]:
        y += 15
    if pg.key.get_pressed()[K_a]:
        x -= 15
    if pg.key.get_pressed()[K_d]:
        x += 15

    pg.display.update()
