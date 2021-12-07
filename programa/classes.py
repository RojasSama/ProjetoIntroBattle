import pygame as pg

class Character():
    catalog = {
        'mago': pg.transform.scale2x(pg.image.load('Personagens/mago(final).png')),
        'bruxa': pg.transform.scale2x(pg.image.load('Personagens/bruxa.png')),
        'vampiro': pg.transform.scale2x(pg.image.load('Personagens/vampiro.png')),
        'caveira': pg.transform.scale2x(pg.image.load('Personagens/caveira.png')),
        'clerigo': pg.transform.scale2x(pg.image.load('Personagens/clerigo(sem_sombra).png')),
        'paladino': pg.transform.scale2x(pg.image.load('Personagens/paladino.png')),
        'cacadora': pg.transform.scale2x(pg.image.load('Personagens/cacadora.png')),
    }
    '''    
    Atributes:
        hp : character health points,
        atk : character attack points,
        df : character defense points,
        spd : character speed,
    '''
    def __init__(self, hp, atk, df, spd, defeat=False):
        self.hp = hp
        self.atk = atk
        self.df = df
        self.spd = spd
        self.defense = defeat
        

    def attack(self, inimigo):
        damage = (self.atk * 50) // 50 + (inimigo.df * 2)
        inimigo.hp += damage

    def defensor(self, damage):
        self.hp += damage

    def verifies_defeat(self):
        if self.hp == 0:
            self.defense = True
    
    def blit_character(self, x, y, img, screen):
        screen.blit(img, (x, y))
        

class Battle(Character):
    '''
    Atributes:
        c2 : character 2,
        c3 : character 3,
    '''
    def __init__(self, c1, c2, c3, e1, e2, e3):
        Character.__init__(c1, c2, c3, e1, defeat=False)
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
    
    def blit_characters(self):
        pass
    