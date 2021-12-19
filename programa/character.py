import pygame as pg


class Character():
    '''
    Atributes:
        hp : character health points,
        atk : character attack points,
        df : character defense points,
        spd : character speed,
    '''
    def __init__(self):  # standard atributes
        self.health = 80
        self.attack = 8
        self.defense = 10
        self.speed = 2
        self.defeat = False
        
        self.ui_bg = pg.transform.scale(pg.image.load('UI/introcomp_menu(resized).png'), (150, 150))
        self.shadow = pg.image.load('UI/introcomp_character.png')
        self.catalog = {  # catalogo de sprites dos personagens
            'wizard': pg.transform.flip(pg.transform.scale(pg.image.load('Personagens/mago(final).png'), (90, 90)), True, False),
            'witch': pg.transform.scale(pg.image.load('Personagens/bruxa.png'), (90, 90)),
            'rogue': pg.transform.scale(pg.image.load('Personagens/vampiro.png'), (90, 90)),
            'skeleton': pg.transform.scale(pg.image.load('Personagens/caveira.png'), (90, 90)),
            'priest': pg.transform.scale(pg.image.load('Personagens/clerigo(sem_sombra).png'), (90, 90)),
            'paladin': pg.transform.scale(pg.image.load('Personagens/paladino.png'), (90, 90)),
            'hunter': pg.transform.scale(pg.image.load('Personagens/cacadora.png'), (90, 90)),
        }

    def attack_enemy(self, enemy):
        damage = (self.attack * 50) // 50 + (enemy.df * 2)
        enemy.hp += damage

    def defend(self, damage):
        self.health += damage

    def verifies_defeat(self):
        if self.health == 0:
            self.defeat = True
    
    def blit_character(self, x, y, img, screen):
        screen.blit(img, (x, y))

class Wizard(Character):
    def __init__(self):
        super().__init__(self)
        self.heath = 80
        self.attack = 8
        self.defense = 5
        self.speed = 1
        self.img = self.catalog['wizard']

class Witch(Character):
    def __init__(self):
        super().__init__(self)
        self.health = 75
        self.attack = 9
        self.defense = 4
        self.speed = 3
        self.img = self.catalog['witch']

class Rogue(Character):
    def __init__(self):
        super().__init__(self)
        self.health = 85
        self.attack = 10
        self.defense = 2
        self.speed = 5
        self.img = self.catalog['Rogue']

class Skeleton(Character):
    def __init__(self):
        super().__init__(self)
        self.health = 70
        self.attack = 11
        self.defense = 6
        self.speed = 4
        self.img = self.catalog['Skeleton']

class Priest(Character):
    def __init__(self):
        super().__init__(self)
        self.health = 80    
        self.attack = 7
        self.defense = 8
        self.speed = 4
        self.img = self.catalog['Priest']

class Paladin(Character):
    def __init__(self):
        super().__init__(self)
        self.health = 90
        self.attack = 5
        self.defense = 6
        self.speed = 1
        self.img = self.catalog['Paladin']

class Hunter(Character):
    def __init__(self):
        super().__init__(self)
        self.health = 85
        self.attack = 6
        self.defense = 3
        self.speed = 5
        self.img = self.catalog['Hunter']
