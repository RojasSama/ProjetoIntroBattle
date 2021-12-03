import pygame


class Character():
    catalog = {
        'bruxa': pygame.transform.scale2x(pygame.image.load('Personagens/bruxa.png')),
        'cacadora': pygame.transform.scale2x(pygame.image.load('Personagens/cacadora.png')),
        'caveira': pygame.transform.scale2x(pygame.image.load('Personagens/caveira.png')),
        'clerigo': [pygame.transform.scale2x(pygame.image.load('Personagens/clerigo(com_sombra.png)')), pygame.transform.scale2x(pygame.image.load('Personagens/clerigo(sem_sombra.png)'))],
        'mago': pygame.transform.scale2x(pygame.image.load('Personagens/mago(final).png')),
        'paladino': pygame.transform.scale2x(pygame.image.load('Personagens/paladino.png')),
        'vampiro': pygame.transform.scale2x(pygame.image.load('Personagens/vampiro.png')),
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
    
    def blit_character(self, x, y, img):
        pass
        

class Battle(Character):
    '''
    Atributes:
        c1 : character 1,
        c2 : character 2,
        c3 : character 3,
        e1 : enemy 1,
        e2 : enemy 2,
        e3 : enemy 3
    '''
    def __init__(self, c1, c2, c3, e1, e2, e3):
        # Character.__init__(self, hp, atq, df, vl, defeat=False)
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
    