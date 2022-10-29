import pygame, sys
from bullet import Bullet
from ino import Ino
import time

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

def update(bg_color, screen, gun, inos, bullets):
    '''обновление экрана'''
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, inos, bullets):
    '''обновлять позиции пуль'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)
    # TODO print(len(bullets))

def gun_kill(stats, screen, gun, bullets, inos):
    '''столкновение пушки и армии'''
    stats.guns_left -= 1
    inos.empty()
    bullets.empty()
    create_army(screen, inos)
    time.sleep(1)

def update_inos(stats, screen, inos, gun, bullets):
    '''обновление позиций инопланетян'''
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, gun, bullets, inos)
    inos_check(stats, screen, gun, inos, bullets)

def inos_check(stats, screen, gun, inos, bullets):
    '''проверка добралась ли армия до конца экрана'''
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, bullets, inos)
            break


def create_army(screen, inos):
    '''создание армии пришельцев'''
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 9):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height +  (ino.rect.height * row_number)
            inos.add(ino)