import sys
from turtle import Screen
import pygame
import settings
from ship import Ship
from bullet import Bullet

def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
         bullet.draw_bullet()   # ✅ 必须是 draw_bullet

    ship.blitme()
    #r让最近绘制的屏幕可见
    pygame.display.flip()
def check_events(ai_settings,screen,ship,bullets):#重构check_events函数后，专门负责循环和分发事件
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
             check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
         
def check_keydown_events(event,ai_settings,screen,ship,bullets):#新函数：专门处理按键按下
        """响应按键"""
        
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key ==pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
             fire_bullet(ai_settings,screen,ship,bullets)
def fire_bullet(ai_settings,screen,ship,bullets):
   """如果还没有达到限制,就发射一颗子弹"""
   #创建新子弹，并将其加入到编组bullets中
   if len(bullets) < ai_settings.bullet_allowed: 
           new_bullet = Bullet(ai_settings,screen,ship)
           bullets.add(new_bullet)        

def check_keyup_events(event,ship):#新函数，处理按键松开
        """响应按键松开"""
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

