
class GameStats():
    """跟踪游戏统计信息"""

    def __init__(self, settings):
        """初始化统计信息"""
        self.settings = settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = True

        self.high_score = 0

    def reset_stats(self):
        """初始化游戏运行期间课变化的统计信息"""
        self.ships_left = self.settings.wbc_limit
        self.score = 0
        self.level = 1
