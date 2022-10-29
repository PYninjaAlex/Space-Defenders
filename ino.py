import pygame

class Ino(pygame.sprite.Sprite):
    '''Класс одного пришельца'''

    def __init__(self, screen):
        '''инициализируем и создаём начальную позицию'''
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        '''вывод пришельца на экран'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''перемещение прешельцев'''
        self.y += 0.05
        self.rect.y = self.y


