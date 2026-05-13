import pygame
import os

class SoundManager():
    """管理游戏音效的类"""
    # ============== 新增：音效管理器 ==============
    
    def __init__(self):
        """初始化音效系统"""
        pygame.mixer.init()
        
        # 获取声音文件目录
        sound_dir = 'sounds'
        
        # ============== 加载音效文件 ==============
        # 射击音效
        self.shoot_sound = self.load_sound(os.path.join(sound_dir, 'shoot.wav'))
        
        # 外星人爆炸音效
        self.explosion_sound = self.load_sound(os.path.join(sound_dir, 'explosion.wav'))
        
        # 飞船被撞音效
        self.ship_hit_sound = self.load_sound(os.path.join(sound_dir, 'ship_hit.wav'))
        
        # 游戏结束音效
        self.game_over_sound = self.load_sound(os.path.join(sound_dir, 'game_over.wav'))
    
    def load_sound(self, filename):
        """加载声音文件"""
        if os.path.exists(filename):
            return pygame.mixer.Sound(filename)
        else:
            print(f"警告：找不到音效文件 {filename}，将使用静默")
            # 返回一个静默的音效对象
            return None
    
    def play_shoot(self):
        """播放射击音效"""
        if self.shoot_sound:
            self.shoot_sound.play()
    
    def play_explosion(self):
        """播放爆炸音效"""
        if self.explosion_sound:
            self.explosion_sound.play()
    
    def play_ship_hit(self):
        """播放飞船被撞音效"""
        if self.ship_hit_sound:
            self.ship_hit_sound.play()
    
    def play_game_over(self):
        """播放游戏结束音效"""
        if self.game_over_sound:
            self.game_over_sound.play()
