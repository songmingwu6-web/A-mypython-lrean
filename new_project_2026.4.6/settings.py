class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width =1200
        self.screen_height =800
        self.bg_color = (230,230,230)
        #飞船设置
        self.ship_limit = 3#飞船最大数量
        #子弹设置
        
        self.bullet_width = 3  #测试时子弹宽度设置为300，实际游戏中设置为3
        self.bullet_height = 15
        self.bullet_color = (128,0,255)
        self.bullet_allowed = 3
         # 外星人设置
        self.fleet_drop_speed = 10 # 外星人向下移动的速度
        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.intialize_dynamic_settings()
    def intialize_dynamic_settings(self): 
        """初始化游戏随游戏进行而变化的设置"""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.1 # 数值可以自己调，比如 0.5 或 1
        # 1 表示向右移动，-1 表示向左移动
        self.fleet_direction = 1 
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        

        
     