#jh.py
import pygame

class JH:
    def __init__(self, screen):
        self.screen = screen

        # 尝试加载图片
        # 尝试加载图片（注意文件名是小写的 jh.bmp）
        try:
            self.image = pygame.image.load('images/jh.bmp')
            self.image = pygame.transform.scale(self.image, (150, 150))
        except pygame.error as e:
            print(f"Error loading image: {e}")
            # 修正拼写错误：将 surfase 改回 Surface，并填入白色背景 (255, 255, 255)
            self.image = pygame.Surface((150, 150))
            self.image.fill((255, 255, 255))
        
        # 获取屏幕的矩形区域
        self.screen_rect = screen.get_rect()

        # 创建一个 rect 对象用于定位，并设置在屏幕底部中央
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)