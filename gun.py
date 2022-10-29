import pygame

class Gun:
    def __init__(self, screen):
        """инициализация пушки"""

        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.mright = False
        # self.mleft = False
        self.speed = 0


    def output(self):
        '''рисование пушки'''
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        ''''обновление позиции пушки'''
        self.rect.centerx += self.speed
        if  self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
            # self.mright = False
            # self.rect.centerx -= 1
            # self.mleft = False

    def create_gun(self):
        '''размещает пушку по центру внизу'''
        self.center = self.screen_rect.centerx