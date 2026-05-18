import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship  # Ensure ship.py is in the same directory as this script, or check the filename and path
from alien import Alien
import game_function as gf
from game_stats import GameStats
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建外星人群
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, ship, aliens, bullets)
        
        ship.update()
        gf.update_bullets(ai_settings, screen, ship,bullets, aliens)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.check_bullet_alien_collisions(ai_settings,stats, screen, ship, bullets, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()