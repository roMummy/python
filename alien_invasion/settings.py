class Settings():
    def __init__(self):
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船的速度
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 100
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        #外星人设定
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100
        self.ship_limit = 3 #玩家生命
        #移动方向 1向右 -1向左
        self.fleet_direction = 1
