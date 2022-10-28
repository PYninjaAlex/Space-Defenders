import pygame, sys
from bullet import Bullet

def events(screen, gun, bullets):
    '''обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # кнопка вправо
            if event.key == pygame.K_d:
                gun.speed += 1
            elif event.key == pygame.K_a:
                gun.speed -= 1
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # кнопка вправо
            if event.key == pygame.K_d:
                gun.speed -= 1
            elif event.key == pygame.K_a:
                gun.speed += 1

def update(bg_color, screen, gun, bullets):
    '''обновление экрана'''
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()

def update_bullets(bullets):
    '''обновлять позиции пуль'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)