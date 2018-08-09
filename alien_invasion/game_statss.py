###游戏数据统计###

class GameStatss():
    """跟踪统计游戏信息"""
    def __init__(self, ai_setting):
        """初始化统计数据"""
        self.ai_setting = ai_setting
        self.reset_stats()

        #游戏启动时处于活动状态
        self.game_active = True

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_setting.ship_limit