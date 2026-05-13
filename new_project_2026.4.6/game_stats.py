class GameStats():
    """跟踪游戏的统计信息"""
    # ============== 新增：游戏统计类 ==============
    
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True  # 游戏活动标志
        
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = 3  # 初始飞船数量
        self.score = 0  # 初始得分
