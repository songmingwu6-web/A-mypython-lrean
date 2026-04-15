# man.py
import pygame

class Man:
    def __init__(self, screen):
        self.screen = screen
        
        try:
            self.images = pygame.image.load('images/man.bmp')
        except pygame.error as e:
            print(f"无法加载图片: images/man.bmp - {e}")
            self.images = pygame.Surface((50, 50))
            self.images.fill((255, 0, 0))
        
        # 缩放到 50x50
        self.images = pygame.transform.scale(self.images, (50, 50))
        
        self.rect = self.images.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.images, self.rect)