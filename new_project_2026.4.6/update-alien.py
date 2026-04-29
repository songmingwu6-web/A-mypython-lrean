import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship  # Ensure ship.py is in the same directory as this script, or check the filename and path
import game_function as gf
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        #把之前的update_bullets函数放到game_function.py中，现在直接调用即可
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()