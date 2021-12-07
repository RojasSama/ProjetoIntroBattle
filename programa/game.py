import pygame

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.z_KEY, self.x_KEY, self.RIGHT_KEY, self.LEFT_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1024, 768
        self.display = pygame.Surface((self.DISPLAY_H, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = 'FreePixel.ttf'
        self.font_name = pygame.font.get.get_default_font()

        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.z_KEY = True
                if event.key == pygame.K_x:
                    self.x_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
            