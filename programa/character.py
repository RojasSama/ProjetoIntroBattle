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
        self.defending = False
        self.defeat = False
        self.ui_bg = pg.transform.scale(pg.image.load('UI/introcomp_menu(resized).png'), (150, 150))
        self.shadow = pg.image.load('UI/introcomp_character.png')
        self.catalog = {  # catalogo de sprites dos personagens
            'Wizard': pg.transform.flip(pg.transform.scale(pg.image.load('Personagens/mago(final).png'), (90, 90)), True, False),
            'Witch': pg.transform.scale(pg.image.load('Personagens/bruxa.png'), (90, 90)),
            'Rogue': pg.transform.scale(pg.image.load('Personagens/vampiro.png'), (90, 90)),
            'Skeleton': pg.transform.scale(pg.image.load('Personagens/caveira.png'), (90, 90)),
            'Priest': pg.transform.scale(pg.image.load('Personagens/clerigo(sem_sombra).png'), (90, 90)),
            'Paladin': pg.transform.scale(pg.image.load('Personagens/paladino.png'), (90, 90)),
            'Hunter': pg.transform.scale(pg.image.load('Personagens/cacadora.png'), (90, 90)),
        }

    def attack_enemy(self, enemy):
        damage = (self().show_attack() * 50) // 50 + (enemy().health * 2)
        enemy().health += damage

    def defend(self):
        self.defending = True

    def verifies_defeat(self):
        if self.health == 0:
            self.defeat = True
        return True
    
    def blit_character(self, x, y, img, screen):
        if not (self.defeat):
            screen.blit(img, (x, y))
    
    def show_hp(self):
        return self.health
    
    def show_attack(self):
        return self.attack
    
    def show_defense(self):
        return self.defense

    def show_speed(self):
        return self.speed

class Wizard(Character):
    def __init__(self):
        Character.__init__(self)
        self.defending = False
        self.health = 80
        self.attack = 8
        self.defense = 5
        self.speed = 1
        self.img = self.catalog['Wizard']

class Witch(Character):
    def __init__(self):
        Character.__init__(self)
        self.defending = False
        self.health = 75
        self.attack = 9
        self.defense = 4
        self.speed = 3
        self.img = self.catalog['Witch']

class Rogue(Character):
    def __init__(self):
        Character.__init__(self)
        self.defending = False
        self.health = 85
        self.attack = 10
        self.defense = 2
        self.speed = 5
        self.img = self.catalog['Rogue']

class Skeleton(Character):
    def __init__(self):
        Character.__init__(self)
        self.defending = False
        self.health = 70
        self.attack = 11
        self.defense = 6
        self.speed = 4
        self.img = self.catalog['Skeleton']

class Priest(Character):
    def __init__(self):
        Character.__init__(self)
        self.defending = False
        self.health = 80    
        self.attack = 7
        self.defense = 8
        self.speed = 4
        self.img = self.catalog['Priest']

class Paladin(Character):
    def __init__(self):
        Character.__init__(self)
        self.defending = False
        self.health = 90
        self.attack = 5
        self.defense = 6
        self.speed = 1
        self.img = self.catalog['Paladin']

class Hunter(Character):
    def __init__(self):
        Character.__init__(self)
        self.defending = False
        self.health = 85
        self.attack = 6
        self.defense = 3
        self.speed = 5
        self.img = self.catalog['Hunter']
