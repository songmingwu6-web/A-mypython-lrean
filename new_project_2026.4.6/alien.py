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
        self.rect.center = (600, 300)
    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image, self.rect)

      



       