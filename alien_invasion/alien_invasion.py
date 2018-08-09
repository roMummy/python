import sys
import pygame
from settings import  Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import  Alien
from game_statss import GameStatss

def run_game():
    #初始化游戏 创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("打飞机")

    #创建一个用于存储游戏统计信息的实例
    stats = GameStatss(ai_settings)

    #创建一个飞船
    ship = Ship(screen, ai_settings)
    #创建一个外星人
    alien = Alien(ai_settings, screen)

    #创建一个用于存储子弹的数组
    bullets = Group()
    #创建一个用于存储外星人的数组
    aliens = Group()
    # 添加外星人
    gf.create_fleet(ai_settings, screen, aliens, ship)

    #游戏主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ship, ai_settings, screen, bullets)

        if stats.game_active:

            ship.update()

            #更新子弹
            gf.update_bullets(bullets, aliens, ai_settings,screen, ship)

            #更新外星人的位置
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)

        #更新场景
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()
