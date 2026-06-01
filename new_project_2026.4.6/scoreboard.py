import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard():
    """显示得分信息的类"""
    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分相关的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #显示得分信息室使用的字体设置
        self.text_color = (30,30,30)
        # 使用系统字体，指定具体字体名称避免路径解析问题
        # 使用系统默认字体，避免特定字体名称导致的缓存问题
        self.font = pygame.font.Font(None, 48)
        #包含得分图像和最高得分图像的属性
        self.prep_score()
        self.prep_high_score()#显示最高得分数
        self.prep_level()#显示等级
        self.prep_ships()#初始化飞船 
    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20
    def prep_high_score(self):
        """将最高得分转换为一幅渲染的图像"""
        rounded_high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        #将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    def prep_level(self):
        """将等级转换为一幅渲染的图像"""
        self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
        #将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships =Group()#空编组储存飞船实例
        for ship_number in range(self.stats.ships_left):#有多少飞船循环多少次
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10+ship_number*ship.rect.width#左边距为10像素
            ship.rect.y = 10#y坐标为10像素
            self.ships.add(ship)#添加飞船实例到镂空编组中
    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #绘制飞船
        self.ships.draw(self.screen)

        