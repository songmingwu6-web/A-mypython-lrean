import sys
import pygame
import settings
from ship import Ship
from bullet import Bullet
from alien import Alien

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()   # ✅ 必须是 draw_bullet
    ship.blitme()
    # ✅ 正确绘制外星人群，不要用循环，直接调用aliens.draw(screen)即可
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()

# ============== 修改：添加 stats 和 aliens 参数 ==============
def check_events(ai_settings, screen, stats, ship, bullets, aliens, sound):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # ============== 修改：传递所有参数 ==============
            check_keydown_events(event, ai_settings, screen, stats, ship, bullets, aliens, sound)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
# ============== 修改：添加 stats 和 aliens 参数 ==============
def check_keydown_events(event, ai_settings, screen, stats, ship, bullets, aliens, sound):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # ============== 修改：传递 sound 参数 ==============
        fire_bullet(ai_settings, screen, ship, bullets, sound)
    elif event.key == pygame.K_q:
        sys.exit()
    # ============== 新增：按 P 键重新开始游戏 ==============
    elif event.key == pygame.K_p and not stats.game_active:
        reset_game(ai_settings, screen, stats, ship, bullets, aliens, sound)

# ============== 新增：重新开始游戏函数 ==============
def reset_game(ai_settings, screen, stats, ship, bullets, aliens, sound):
    """重新开始游戏"""
    stats.reset_stats()
    stats.game_active = True
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def fire_bullet(ai_settings, screen, ship, bullets, sound):
    """如果还没有达到限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullet_allowed: 
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        # ============== 新增：播放射击音效 ==============
        if sound:
            sound.play_shoot()        

def check_keyup_events(event, ship):
    """响应按键松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

# ============== 修改：更新函数签名和功能扩展 ==============
def update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sound):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # ============== 新增：检查子弹与外星人碰撞 ==============
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens, stats, sound)

# ============== 新增：子弹与外星人碰撞检测 ==============
def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens, stats, sound):
    """响应子弹和外星人的碰撞"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        stats.score += 10  # ============== 新增：加分 ==============
        # ============== 新增：播放爆炸音效 ==============
        if sound:
            sound.play_explosion()
    
    if len(aliens) == 0:  # ============== 新增：外星人全部消灭后创建新舰队 ==============
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
def get_number_aliens_x(ai_settings,screen,alien_width):
     """计算每行可容纳多少外星人"""
     avaliable_space_x = ai_settings.screen_width - 2*alien_width
     number_aliens_x = int(avaliable_space_x/(2*alien_width))
     return number_aliens_x
def get_number_rows(ai_settings,screen,ship,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - ship.rect.height - 3*alien_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并将其放到当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width +2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)


#新增外星部分
def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行能容纳多少个外星人
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_aliens_x = get_number_aliens_x(ai_settings,screen,alien_width)
    #创建第一行外星人
    for alien_number in range(number_aliens_x):
       for row_number in range(get_number_rows(ai_settings,screen,ship,alien_height)):  
           create_alien(ai_settings,screen,aliens,alien_number,row_number)
def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
# ============== 新增：外星人更新函数 ==============
def update_aliens(ai_settings, screen, stats, ship, aliens, bullets, sound):
    """检查是否有外星人位于屏幕边缘，并更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # ============== 新增：检测飞船与外星人碰撞 ==============
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, ship, aliens, bullets, sound)
    
    # ============== 新增：检测外星人到达底部 ==============
    check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets, sound)

# ============== 新增：飞船被撞处理函数 ==============
def ship_hit(ai_settings, screen, stats, ship, aliens, bullets, sound):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # ============== 新增：播放飞船被撞音效 ==============
        if sound:
            sound.play_ship_hit()
        
        stats.ships_left -= 1  # ============== 减少飞船数量 ==============
        aliens.empty()  # ============== 清空外星人 ==============
        bullets.empty()  # ============== 清空子弹 ==============
        create_fleet(ai_settings, screen, ship, aliens)  # ============== 创建新外星舰队 ==============
        ship.center_ship()  # ============== 飞船居中 ==============
    else:
        stats.game_active = False  # ============== 游戏结束 ==============
        # ============== 新增：播放游戏结束音效 ==============
        if sound:
            sound.play_game_over()

# ============== 新增：外星人到达底部检测 ==============
def check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets, sound):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, ship, aliens, bullets, sound)
            break
        
