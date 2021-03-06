import sys
import pygame
from bullet import  Bullet
from alien import  Alien
from time import sleep

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    if event.key == pygame.K_q:
        print("quit")
        sys.exit()

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship, ai_setting, screen, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_setting, screen, bullets)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets, aliens):
    """更新屏幕上的图像，并切换到新屏幕上"""
    # 背景颜色
    screen.fill(ai_settings.bg_color)

    #在飞船后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # aliens.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets, aliens, ai_setting, screen, ship):
    """更新子弹位置，删除消失的子弹"""
    #更新位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 检查是否击中了外星人 击中就删除子弹
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 如果外新人全部消失了
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_setting, screen, aliens, ship)

def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹，加入到编租中
    if ai_settings.bullet_allowed > len(bullets):
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - (3*alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return  number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容下多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #创建一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """有外星人到边缘时做的事情"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_setting, aliens):
    """将外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1

def update_aliens(ai_settings, aliens, ship, stats, screen, bullets):
    """检查是否有外星人位于屏幕边缘，并更新外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    aliens.update()

    #检查外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        print("game over!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

def ship_hit(ai_setting, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0 :
        #将ships_left减1
        stats.ships_left -= 1

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外新人，并将飞船放到低端
        create_fleet(ai_setting, screen, aliens, ship)
        ship.center_ship()

        #暂停
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets):
    """检查外星人是否到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
            break



