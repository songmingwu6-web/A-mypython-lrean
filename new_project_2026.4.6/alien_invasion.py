import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats  # ============== 新增：导入游戏统计类 ==============
from sound import SoundManager  # ============== 新增：导入音效管理器 ==============
import game_function as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    stats = GameStats(ai_settings)  # ============== 新增：创建游戏统计实例 ==============
    sound = SoundManager()  # ============== 新增：创建音效管理器实例 ==============
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    while True:
        # ============== 修改：传递 stats、aliens 和 sound 参数 ==============
        gf.check_events(ai_settings, screen, stats, ship, bullets, aliens, sound)
        
        if stats.game_active:  # ============== 新增：只有游戏活动时才更新 ==============
            ship.update()
            # ============== 修改：传递所有必要参数（包括 sound）==============
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sound)
            gf.update_aliens(ai_settings, screen, stats, ship, aliens, bullets, sound)
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()