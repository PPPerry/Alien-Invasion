import os

class Settings(): #存储设置
    
    def __init__(self): #初始化游戏设置
       os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (150,30) #设置窗口位置
       self.screen_width = 1200
       self.screen_height = 800
       self.bg_color = (230,230,230)

       self.ship_speed_factor = 1.5 #飞船的设置
       self.ship_limit = 3

       self.bullet_speed_factor = 2 #子弹的设置
       self.bullet_width = 3
       self.bullet_height = 15
       self.bullet_color = (60,60,60)
       self.bullets_allowed = 3

       self.alien_speed_factor = 5 #外星人设置
       self.fleet_drop_speed = 10
       self.fleet_direction = 1 #1为右移，-1为左移

