import sys
import pygame
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
    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()