class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏启动时处于非活动状态
        self.game_active = False
        #最高得分在运行期间不应被重置
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        #在reset_stats()方法中添加等级属性
        self.score = 0
        self.level = 1
        