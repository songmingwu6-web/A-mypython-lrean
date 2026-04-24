import sys
import pygame
from ship import Ship

def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #r让最近绘制的屏幕可见
    pygame.display.flip()
def check_events(ship):#重构check_events函数后，专门负责循环和分发事件
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
             check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
         
def check_keydown_events(event,ship):#新函数：专门处理按键按下
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key ==pygame.K_LEFT:
            ship.moving_left = True
def check_keyup_events(event,ship):#新函数，处理按键松开
        """响应按键松开"""
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
            

