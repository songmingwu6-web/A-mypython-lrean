import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.settings = ai_settings

        # 加载图像
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 初始位置：左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 精确位置
        self.x = float(self.rect.x)
       
    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        """向左或向右移动外星人"""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = int(self.x)
       
    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image, self.rect)

      



       